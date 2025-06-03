# 💤 WakeMotion – Detector de Acordar Repentino

## 🎯 Descrição do Problema
Durante quedas de energia, é comum que profissionais de plantão, vigias ou pessoas em abrigos acabem cochilando. Caso haja uma emergência, movimentos bruscos de acordar podem ser um indício de alerta, susto ou reação instintiva. Em ambientes escuros ou silenciosos, essa informação pode ser útil para acionar sistemas auxiliares ou registrar o comportamento do ocupante.

## 💡 Solução Proposta
WakeMotion é uma solução desenvolvida em Python com MediaPipe que detecta, em vídeos simulando ambientes de baixa iluminação, se uma pessoa passa do estado de repouso (deitada) para o estado acordado (sentado ou em pé). A detecção é feita com base na diferença vertical entre os pontos do **nariz** e do **quadril**, utilizando visão computacional para interpretar essa mudança postural como "acordar repentino".

---

## 🧪 Tecnologias Utilizadas
- Python 3.9+
- OpenCV
- MediaPipe

---

## 🎥 Demonstração (vídeo até 3 minutos)
[🔗 Link para o vídeo demonstrativo no YouTube (inserir link aqui)](#)

No vídeo, é possível ver:
- A explicação do problema
- O funcionamento do código
- Um teste real com vídeo simulado
- A exibição das mensagens "PESSOA EM REPOUSO" e "PESSOA ACORDOU!" na tela

---

## 💻 Como Executar Localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/wakemotion.git
cd wakemotion
````

### 2. Instale as dependências:

```bash
pip install opencv-python mediapipe
```

### 3. Substitua o vídeo `video-teste.mp4` pelo seu vídeo de simulação

### 4. Execute o script:

```bash
python acordar_movimento.py
```

### 5. Pressione `Q` para sair da visualização.

---

## 🧠 Lógica de Funcionamento

* A cada frame do vídeo, o sistema verifica a distância vertical entre os pontos do **nariz** e do **quadril esquerdo**.
* Se a diferença for **pequena** (posição deitada), o sistema exibe:
  ✅ `PESSOA EM REPOUSO`
* Se a diferença for **grande** (posição sentada ou em pé), o sistema exibe:
  ⚠️ `PESSOA ACORDOU!`

---

## 👨‍🏫 Integrantes

| Nome completo            | RM     |
| ------------------------ | ------ |
| Lucas Laia Manentti      | 97709  |
| Rony Ken Nagai           | 551549 |
| Tomáz Versolato Carballo | 551417 |

---

## 📌 Observações

* Você pode ajustar o limiar de sensibilidade (`diferenca_nariz_quadril > 0.3`) conforme o vídeo utilizado.
* O sistema funciona melhor com vídeos com **mínima iluminação** (sem estar completamente escuro).