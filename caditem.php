<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    // Se o usuário não estiver logado, redireciona para a página de login
    header('Location: admin.php');
    exit;
}

$servername = "localhost";
$port = 3306;
$username = "root";
$password = "";
$dbname = "ferramentaria";

try {
    $conn = new PDO("mysql:host=$servername;port=$port;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Erro na conexão com o banco de dados: " . $e->getMessage();
}

function displayEstoque($conn)
{
    $sql = "SELECT * FROM estoque";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    echo "<table>";
    echo "<td><h3>Cadastro de Itens - Estoque Ferramentaria </h3></td>";
    echo "<tr><th>ID</th><th>Item</th><th>Quantidade</th><th>Imagem</th><th>Ações</th></tr>";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr>";
        echo "<td>{$row['id']}</td>";
        echo "<td>{$row['item']}</td>";
        echo "<td>{$row['quantidade']}</td>";
        echo "<td><img src='uploads/{$row['imagem']}' style='width:100px;height:100px;'></td>";
        echo "<td>";
        echo "<button style='margin-right: 5px;' onclick='openModal(\"{$row['id']}\", \"{$row['item']}\", \"{$row['quantidade']}\", \"{$row['imagem']}\")'>Editar</button>";
        echo "<form method='post' action='admin.php'>";
        echo "<input type='hidden' name='delete_id' value='{$row['id']}'>";
        echo "<button type='submit' name='delete'>Excluir</button>";
        echo "</form>";
        echo "</td>";
        echo "</tr>";
    }
    echo "</table>";
}

function addItem($conn, $item, $quantidade, $imagem)
{
    $sql = "INSERT INTO estoque (item, quantidade, imagem) VALUES (:item, :quantidade, :imagem)";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':item', $item);
    $stmt->bindParam(':quantidade', $quantidade);
    $stmt->bindParam(':imagem', $imagem);
    $stmt->execute();
}

function updateItem($conn, $id, $item, $quantidade, $imagem, $imagem_temp)
{
    // Verifica se uma nova imagem foi fornecida
    if (!empty($imagem_temp)) {
        // Se uma nova imagem foi fornecida, move e atualiza o registro com a nova imagem
        move_uploaded_file($imagem_temp, "uploads/$imagem");
        $sql = "UPDATE estoque SET item = :item, quantidade = :quantidade, imagem = :imagem WHERE id = :id";
    } else {
        // Se nenhuma nova imagem foi fornecida, mantém a imagem existente no banco de dados
        $sql = "UPDATE estoque SET item = :item, quantidade = :quantidade WHERE id = :id";
    }

    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':item', $item);
    $stmt->bindParam(':quantidade', $quantidade);
    // Se nenhuma nova imagem foi fornecida, vincula a imagem existente
    if (!empty($imagem_temp)) {
        $stmt->bindParam(':imagem', $imagem);
    }
    $stmt->execute();
}

function deleteItem($conn, $id)
{
    $sql = "DELETE FROM estoque WHERE id = :id";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':id', $id);
    $stmt->execute();
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['add'])) {
    $item = $_POST['item'];
    $quantidade = $_POST['quantidade'];
    $imagem = $_FILES['imagem']['name'];
    $imagem_temp = $_FILES['imagem']['tmp_name'];
    move_uploaded_file($imagem_temp, "uploads/$imagem");
    addItem($conn, $item, $quantidade, $imagem);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['update'])) {
    $id = $_POST['item_id'];
    $item = $_POST['item'];
    $quantidade = $_POST['quantidade'];
    $imagem = $_FILES['imagem']['name'];
    $imagem_temp = $_FILES['imagem']['tmp_name'];
    updateItem($conn, $id, $item, $quantidade, $imagem, $imagem_temp);
    header("Location: admin.php");
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete'])) {
    $id = $_POST['delete_id'];
    deleteItem($conn, $id);
    header("Location: admin.php");
}

displayEstoque($conn);

$conn = null;
?>

<div id="editModal" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal()">&times;</span>
        <h3>Editar Item</h3>
        <form method="post" action="admin.php" enctype="multipart/form-data">
            <input type="hidden" id="edit_item_id" name="item_id">
            <input type="text" id="edit_item" name="item" placeholder="item" required>
            <input type="number" id="edit_quantidade" name="quantidade" placeholder="quantidade" required>
            <input type="file" id="edit_imagem" name="imagem" accept="image/*">
            <button type="submit" name="update">Atualizar</button>
        </form>
    </div>
</div>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" enctype="multipart/form-data">
    <input type="text" name="item" placeholder="Digite o nome do Item." required>
    <input type="number" name="quantidade" placeholder="Digite a Quantidade." required>
    <input type="file" name="imagem" accept="image/*" required>
    <button type="submit" name="add">Adicionar</button>
</form>

<div class="logout-container">
    <a href="logout.php" class="logout">Sair</a>
</div>

<script>
    function openModal(id, produto, valor, imagem) {
        document.getElementById('edit_item_id').value = id;
        document.getElementById('edit_item').value = produto;
        document.getElementById('edit_quantidade').value = valor;
        document.getElementById('editModal').style.display = 'block';
    }

    function closeModal() {
        document.getElementById('editModal').style.display = 'none';
    }
</script>