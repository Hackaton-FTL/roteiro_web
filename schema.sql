-- Criação da tabela `categorias`
CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

-- Inserção de categorias de exemplo
INSERT INTO categorias (nome) VALUES
('Cultura'),
('Natureza'),
('Gastronomia'),
('Aventura'),
('Relaxamento'),
('Vida Noturna'),
('Compras'),
('História'),
('Esportes'),
('Lazer');

---

-- Criação da tabela `atividades`
CREATE TABLE atividades (
    id_atividade INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_atividade TEXT NOT NULL,
    duracao_horas REAL,
    id_categoria INTEGER,
    custo REAL,
    descricao TEXT,
    FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria)
);

-- Inserção de atividades de exemplo
-- Categoria: Cultura (id: 1)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Visita a Museu de Arte Moderna', 3.0, 1, 50.00, 'Exposição de obras de artistas renomados.'),
('Passeio pelo Centro Histórico', 4.0, 1, 0.00, 'Caminhada guiada pelas ruas antigas da cidade.'),
('Noite de Teatro', 2.5, 1, 80.00, 'Espetáculo de comédia ou drama no teatro principal.'),
('Galeria de Fotografia', 2.0, 1, 30.00, 'Exposição de fotografias de paisagens e retratos.');

-- Categoria: Natureza (id: 2)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Trilha em Parque Natural', 5.0, 2, 0.00, 'Trilha de nível fácil a moderado com vistas panorâmicas.'),
('Passeio de Caiaque no Lago', 2.0, 2, 75.00, 'Aluguel de caiaque para explorar um lago tranquilo.'),
('Piquenique no Jardim Botânico', 3.0, 2, 10.00, 'Entrada no jardim com espaço para um piquenique.'),
('Observação de Pássaros', 2.0, 2, 20.00, 'Excursão para avistar aves nativas da região.');

-- Categoria: Gastronomia (id: 3)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Tour de Degustação de Vinhos', 2.5, 3, 120.00, 'Visita a vinícola com degustação de vinhos.'),
('Aula de Culinária Local', 3.0, 3, 150.00, 'Aprenda a cozinhar pratos típicos da região.'),
('Mercado de Alimentos Locais', 2.0, 3, 0.00, 'Explorar barracas de comida e ingredientes frescos.');

-- Categoria: Aventura (id: 4)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Escalada em Rocha', 4.0, 4, 200.00, 'Sessão de escalada com instrutor e equipamento.'),
('Tirolesa', 1.0, 4, 90.00, 'Uma experiência de tirolesa sobre paisagem natural.');

-- Categoria: Relaxamento (id: 5)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Sessão de Massagem em Spa', 1.5, 5, 180.00, 'Massagem relaxante em spa de luxo.'),
('Dia na Praia', 6.0, 5, 0.00, 'Passe o dia na praia, relaxando e nadando.');

-- Categoria: Vida Noturna (id: 6)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Bar de Jazz ao Vivo', 3.0, 6, 60.00, 'Ouça música jazz em um ambiente intimista.');
-- Categoria: Compras (id: 7)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Passeio em Shopping Center', 3.0, 7, 0.00, 'Visita a um grande centro comercial.');

-- Categoria: História (id: 8)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Visita a Monumentos Históricos', 3.0, 8, 25.00, 'Tour por monumentos e locais de significado histórico.');

-- Categoria: Esportes (id: 9)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Aula de Yoga no Parque', 1.0, 9, 35.00, 'Sessão de yoga ao ar livre com instrutor.'),
('Aluguel de Bicicleta', 4.0, 9, 45.00, 'Alugue uma bicicleta e explore a cidade.');

-- Categoria: Lazer (id: 10)
INSERT INTO atividades (nome_atividade, duracao_horas, id_categoria, custo, descricao) VALUES
('Ir ao Cinema', 2.0, 10, 40.00, 'Assista a um filme em uma sala de cinema.');