import streamlit as st

st.title("🎈 halo barudak")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Jump Game</title>
    <style>
        /* Gaya Visual Game */
        body { margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f0f0f0; font-family: Arial, sans-serif; }
        #gameCanvas { background: #fff; border-bottom: 2px solid #333; }
        .info { position: absolute; top: 20px; text-align: center; }
    </style>
</head>
<body>

<div class="info">
    <h1>Loncat!</h1>
    <p>Tekan **Spasi** atau **Klik** untuk loncat.</p>
    <h2 id="score">Skor: 0</h2>
</div>
<canvas id="gameCanvas"></canvas>

<script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");

    // Ukuran Canvas
    canvas.width = 600;
    canvas.height = 200;

    // Variabel Game
    let score = 0;
    let gameSpeed = 3;
    let isGameOver = false;

    // Objek Pemain (Kotak Biru)
    const player = {
        x: 50,
        y: 150,
        w: 30,
        h: 30,
        dy: 0,
        jumpForce: 12,
        gravity: 0.6,
        grounded: false
    };

    // Objek Rintangan (Kotak Merah)
    const obstacle = {
        x: canvas.width,
        y: 155,
        w: 25,
        h: 25
    };

    function jump() {
        if (player.grounded && !isGameOver) {
            player.dy = -player.jumpForce;
            player.grounded = false;
        } else if (isGameOver) {
            resetGame();
        }
    }

    // Input Control
    window.addEventListener("keydown", (e) => { if (e.code === "Space") jump(); });
    canvas.addEventListener("mousedown", jump);

    function resetGame() {
        score = 0;
        gameSpeed = 3;
        obstacle.x = canvas.width;
        isGameOver = false;
        requestAnimationFrame(update);
    }

    function update() {
        if (isGameOver) return;

        // Gravitasi & Pergerakan Pemain
        player.dy += player.gravity;
        player.y += player.dy;

        if (player.y + player.h > canvas.height) {
            player.y = canvas.height - player.h;
            player.dy = 0;
            player.grounded = true;
        }

        // Pergerakan Rintangan
        obstacle.x -= gameSpeed;
        if (obstacle.x + obstacle.w < 0) {
            obstacle.x = canvas.width;
            score++;
            gameSpeed += 0.1; // Makin lama makin cepat
        }

        // Cek Tabrakan
        if (
            player.x < obstacle.x + obstacle.w &&
            player.x + player.w > obstacle.x &&
            player.y < obstacle.y + obstacle.h &&
            player.y + player.h > obstacle.y
        ) {
            isGameOver = true;
            alert("Game Over! Skor Akhir: " + score);
            resetGame();
        }

        draw();
        scoreElement.innerText = "Skor: " + score;
        requestAnimationFrame(update);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Gambar Pemain
        ctx.fillStyle = "#3498db";
        ctx.fillRect(player.x, player.y, player.w, player.h);

        // Gambar Rintangan
        ctx.fillStyle = "#e74c3c";
        ctx.fillRect(obstacle.x, obstacle.y, obstacle.w, obstacle.h);
    }

    update();
</script>
</body>
</html>
