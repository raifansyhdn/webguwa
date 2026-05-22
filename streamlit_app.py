import streamlit as st

st.title("🎈 halo barudak")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Jump Game - Fixed</title>
    <style>
        body { margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f0f0f0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; overflow: hidden; }
        #gameCanvas { background: #fff; border-bottom: 3px solid #333; box-shadow: 0 10px 20px rgba(0,0,0,0.1); cursor: pointer; }
        .info { position: absolute; top: 20px; text-align: center; }
    </style>
</head>
<body>

<div class="info">
    <h2 id="score">Skor: 0</h2>
    <p>Klik atau tekan Spasi untuk loncat</p>
</div>
<canvas id="gameCanvas"></canvas>

<script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    const scoreElement = document.getElementById("score");

    canvas.width = 600;
    canvas.height = 200;

    // --- BAGIAN PENANGANAN GAMBAR ---
    let imagesLoaded = 0;
    const totalImages = 2;

    const playerImg = new Image();
    playerImg.src = 'player.png'; // Pastikan file ini ada di GitHub Anda
    playerImg.onload = () => { imagesLoaded++; checkAllLoaded(); };
    playerImg.onerror = () => { useFallback(); }; // Jika gambar error, gunakan kotak warna

    const obstacleImg = new Image();
    obstacleImg.src = 'obstacle.png'; // Pastikan file ini ada di GitHub Anda
    obstacleImg.onload = () => { imagesLoaded++; checkAllLoaded(); };
    obstacleImg.onerror = () => { useFallback(); };

    let useColor = false;
    function useFallback() {
        console.warn("Gambar tidak ditemukan, menggunakan kotak warna sebagai pengganti.");
        useColor = true;
        checkAllLoaded();
    }

    function checkAllLoaded() {
        if (imagesLoaded >= totalImages || useColor) {
            update(); // Mulai game jika semua siap
        }
    }

    // --- LOGIKA GAME ---
    let score = 0;
    let gameSpeed = 4;
    let isGameOver = false;

    const player = { x: 50, y: 150, w: 40, h: 40, dy: 0, jumpForce: 12, gravity: 0.6, grounded: false };
    const obstacle = { x: canvas.width, y: 150, w: 35, h: 40 };

    function jump() {
        if (player.grounded && !isGameOver) {
            player.dy = -player.jumpForce;
            player.grounded = false;
        } else if (isGameOver) {
            location.reload(); // Refresh halaman untuk restart jika error
        }
    }

    window.addEventListener("keydown", (e) => { if (e.code === "Space") jump(); });
    canvas.addEventListener("mousedown", jump);

    function update() {
        if (isGameOver) return;

        player.dy += player.gravity;
        player.y += player.dy;

        if (player.y + player.h > canvas.height) {
            player.y = canvas.height - player.h;
            player.dy = 0;
            player.grounded = true;
        }

        obstacle.x -= gameSpeed;
        if (obstacle.x + obstacle.w < 0) {
            obstacle.x = canvas.width;
            score++;
            gameSpeed += 0.1;
        }

        if (
            player.x < obstacle.x + obstacle.w &&
            player.x + player.w > obstacle.x &&
            player.y < obstacle.y + obstacle.h &&
            player.y + player.h > obstacle.y
        ) {
            isGameOver = true;
            alert("Game Over! Skor: " + score);
            location.reload();
        }

        draw();
        scoreElement.innerText = "Skor: " + score;
        requestAnimationFrame(update);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        if (useColor) {
            ctx.fillStyle = "#3498db";
            ctx.fillRect(player.x, player.y, player.w, player.h);
            ctx.fillStyle = "#e74c3c";
            ctx.fillRect(obstacle.x, obstacle.y, obstacle.w, obstacle.h);
        } else {
            ctx.drawImage(playerImg, player.x, player.y, player.w, player.h);
            ctx.drawImage(obstacleImg, obstacle.x, obstacle.y, obstacle.w, obstacle.h);
        }
    }
</script>
</body>
</html>
