/* ==========================================================================
   CONFIGURAÇÕES GERAIS E TEMA (ESTILO THE BINDING OF ISAAC)
   ========================================================================== */
body {
    background-color: #1a1a1a;
    /* Fundo escuro de calabouço */
    color: #ffffff;
    font-family: 'Courier New', Courier, monospace;
    /* Fonte estilo retrô/terminal */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
    overflow-x: hidden;
}

h1 {
    color: #8b0000;
    /* Vermelho Sangue Escuro */
    text-shadow: 3px 3px 0px #000;
    font-size: 2.5rem;
    margin-bottom: 20px;
    letter-spacing: 2px;
}

h2,
h3 {
    color: #d9d9d9;
    margin-top: 5px;
    text-shadow: 1px 1px 2px #000;
}

/* ==========================================================================
   CONTAINERS E TELAS (LOGIN / REGISTRO)
   ========================================================================== */
.container {
    background: #2a2a2a;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
    border: 2px solid #444;
    text-align: center;
    width: 320px;
    transition: all 0.3s ease;
}

/* Campos de Entrada (Inputs) */
input {
    width: 85%;
    padding: 12px;
    margin: 8px 0;
    border-radius: 4px;
    border: 2px solid #555;
    background: #1c1c1c;
    color: #fff;
    font-size: 14px;
    font-family: inherit;
}

input:focus {
    border-color: #8b0000;
    outline: none;
    box-shadow: 0 0 5px rgba(139, 0, 0, 0.5);
}

/* Botões Estilizados */
button {
    width: 93%;
    padding: 12px;
    border: none;
    background: #8b0000;
    color: white;
    cursor: pointer;
    font-weight: bold;
    font-size: 14px;
    font-family: inherit;
    border-radius: 4px;
    margin: 6px 0;
    text-transform: uppercase;
    box-shadow: 0 4px #5e0000;
    transition: background 0.1s ease, transform 0.1s ease;
}

button:hover {
    background: #b30000;
}

button:active {
    box-shadow: 0 1px #5e0000;
    transform: translateY(3px);
}

/* ==========================================================================
   SISTEMA DE RANKING (TABELA)
   ========================================================================== */
#ranking-box {
    margin-top: 20px;
    padding-top: 15px;
    border-top: 2px dashed #555;
    max-height: 250px;
    overflow-y: auto;
}

table {
    width: 100%;
    margin-top: 10px;
    border-collapse: collapse;
    background: #202020;
    font-size: 14px;
}

th,
td {
    padding: 10px;
    border: 1px solid #444;
    text-align: center;
}

th {
    background: #333;
    color: #ff4d4d;
    font-weight: bold;
}

tr:nth-child(even) {
    background: #262626;
}

/* ==========================================================================
   HUD (INTERFACE DO JOGO) & CANVAS
   ========================================================================== */
#hud {
    display: none;
    /* Ativado via JavaScript */
    width: 600px;
    justify-content: space-between;
    align-items: center;
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 8px;
    background: #2a2a2a;
    padding: 10px 15px;
    border-radius: 4px;
    border: 2px solid #3d312a;
    box-sizing: border-box;
}

#hud-hp {
    color: #ff4d4d;
    font-size: 18px;
    text-shadow: 1px 1px #000;
}

/* Tela de Desenho do Jogo (O Calabouço) */
canvas {
    background: #3d312a;
    /* Cor de chão de terra escura */
    border: 6px solid #2b211c;
    /* Paredes grossas */
    box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.8), 0 8px 20px rgba(0, 0, 0, 0.7);
    display: none;
    /* Ativado via JavaScript */
    border-radius: 4px;
}

/* Classe Utilitária para Esconder Elementos */
.hidden {
    display: none !important;
}
