class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Altura inicial do nó é 1

class AVLTree:
    def insert(self, root, key):
        # Inserção de um nó na árvore AVL
        if not root:
            return Node(key)  # Criar um novo nó se a árvore estiver vazia

        # Inserir na subárvore esquerda ou direita com base no valor da chave
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Atualizar a altura do nó atual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calcular o fator de equilíbrio deste nó
        balance = self.get_balance(root)

        # Caso de desequilíbrio à esquerda
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)  # Rotação simples à direita
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)  # Rotação dupla à direita

        # Caso de desequilíbrio à direita
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)  # Rotação simples à esquerda
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)  # Rotação dupla à esquerda

        return root

    def delete(self, root, key):
        # Exclusão de um nó da árvore AVL
        if not root:
            return root

        # Encontrar e excluir o nó com a chave fornecida
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Encontrar o nó mínimo na subárvore direita
            min_node = self.find_min(root.right)
            root.key = min_node.key
            root.right = self.delete(root.right, min_node.key)

        # Atualizar a altura do nó atual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calcular o fator de equilíbrio deste nó
        balance = self.get_balance(root)

        # Caso de desequilíbrio à esquerda
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)  # Rotação simples à direita
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)  # Rotação dupla à direita

        # Caso de desequilíbrio à direita
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)  # Rotação simples à esquerda
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)  # Rotação dupla à esquerda

        return root

    def search(self, root, key):
        # Pesquisa por uma chave na árvore AVL
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def get_height(self, root):
        # Obtém a altura de um nó (considera nulos como altura 0)
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        # Calcula o fator de equilíbrio de um nó
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, z):
        # Rotação à esquerda
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Atualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, y):
        # Rotação à direita
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        # Atualizar alturas
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def find_min(self, root):
        # Encontra o nó com o valor mínimo na árvore
        while root.left:
            root = root.left
        return root

    def insert_key(self, root, key):
        return self.insert(root, key)

    def delete_key(self, root, key):
        return self.delete(root, key)

    def search_key(self, root, key):
        return self.search(root, key)
