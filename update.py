import base64
import os

img_path = r'C:\Users\umtky\Downloads\WhatsApp Image 2026-05-09 at 21.28.56.jpeg'
with open(img_path, 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anneler Günü Kutlaması</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(-45deg, #0f2a42, #1a3a52, #2c4a6a, #1b263b);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
            position: relative;
        }}

        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* Background Particles */
        .bg-particle {{
            position: fixed;
            bottom: -10px;
            background: rgba(255,255,255,0.4);
            border-radius: 50%;
            box-shadow: 0 0 10px 2px rgba(255,255,255,0.2);
            animation: floatUp linear infinite;
            z-index: 0;
            pointer-events: none;
            will-change: transform, opacity;
        }}
        @keyframes floatUp {{
            0% {{ transform: translateY(0) scale(1); opacity: 0; }}
            10% {{ opacity: 1; }}
            90% {{ opacity: 1; }}
            100% {{ transform: translateY(-105vh) scale(0); opacity: 0; }}
        }}

        .container {{
            text-align: center;
            position: relative;
            width: 100%;
            max-width: 800px;
            padding: 40px 20px;
            z-index: 10;
        }}

        /* Staggered Fade In Up */
        .fade-in-up {{
            opacity: 0;
            transform: translateY(40px);
            animation: fadeInUp 1s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
            will-change: transform, opacity;
        }}
        h1.fade-in-up {{ animation-delay: 0.2s; }}
        .subtitle.fade-in-up {{ animation-delay: 0.3s; }}
        .love-bar-container.fade-in-up {{ animation-delay: 0.5s; }}
        .confetti-button.fade-in-up {{ animation-delay: 0.7s; }}

        @keyframes fadeInUp {{
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        h1 {{
            color: #fff;
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
        }}

        .subtitle {{
            color: #e8d5f2;
            font-size: 1.3em;
            margin-bottom: 40px;
        }}

        /* Photo Reveal */
        .photo-reveal {{
            max-height: 0;
            opacity: 0;
            overflow: hidden;
            transition: all 0.8s ease-out;
            margin-bottom: 0;
            transform: translateY(-50px);
            will-change: transform, opacity, max-height;
        }}

        .photo-reveal.visible {{
            max-height: 1000px;
            opacity: 1;
            transform: translateY(0);
            margin-bottom: 30px;
        }}

        .photo-reveal img {{
            max-width: 100%;
            height: auto;
            border-radius: 20px;
            border: 3px solid #ffd700;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
            max-height: 500px;
            object-fit: cover;
        }}

        .love-message {{
            color: #ffd700;
            font-size: 1.4em;
            margin-top: 15px;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
            opacity: 0;
            transition: opacity 0.5s ease-out 0.8s;
            font-weight: bold;
            font-style: italic;
            will-change: opacity;
        }}
        
        .photo-reveal.visible .love-message {{
            opacity: 1;
        }}

        /* Love Bar */
        .love-bar-container {{
            margin: 40px 0;
            padding: 25px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}

        .love-bar-label {{
            color: #fff;
            font-size: 1.2em;
            margin-bottom: 15px;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .love-bar {{
            width: 100%;
            height: 25px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
            position: relative;
        }}

        .love-fill {{
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #ffd700, #00d4aa, #ff6b9d);
            background-size: 200% 100%;
            border-radius: 20px;
            box-shadow: 0 0 20px #ff6b9d;
            animation: gradientMove 2s linear infinite;
        }}

        @keyframes gradientMove {{
            0% {{ background-position: 100% 0; }}
            100% {{ background-position: -100% 0; }}
        }}

        /* Button */
        .confetti-button {{
            background: linear-gradient(135deg, #ff6b9d, #ff8fab, #00d4aa);
            background-size: 200% auto;
            color: white;
            border: none;
            padding: 18px 50px;
            font-size: 1.2em;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4);
            font-weight: bold;
            margin-top: 20px;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
            will-change: transform, box-shadow;
        }}

        .confetti-button:hover {{
            transform: scale(1.05) translateY(-5px);
            box-shadow: 0 15px 25px rgba(255, 107, 157, 0.6), 0 0 30px rgba(0, 212, 170, 0.4);
            background-position: right center;
        }}

        .confetti-button:active {{
            transform: scale(0.95);
        }}

        /* Heart Icon */
        .heart-icon {{
            display: inline-block;
            margin: 0 5px;
            will-change: transform;
        }}

        .heart-icon.pulse {{
            animation: pulse 2s ease-in-out infinite;
        }}
        
        .heart-icon.fast-beat {{
            animation: fastBeat 0.8s ease-in-out infinite;
            color: #ff6b9d;
            text-shadow: 0 0 10px #ff6b9d;
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}
        
        @keyframes fastBeat {{
            0%, 100% {{ transform: scale(1); }}
            25% {{ transform: scale(1.3); }}
            50% {{ transform: scale(1.1); }}
            75% {{ transform: scale(1.3); }}
        }}

        /* Advanced Confetti */
        .adv-confetti {{
            position: fixed;
            top: -20px;
            z-index: 9999;
            box-shadow: 0 0 8px rgba(255,255,255,0.8);
            pointer-events: none;
            border-radius: 2px;
            will-change: transform, opacity;
        }}

        @keyframes fallTumble {{
            0% {{ transform: translateY(0) rotate3d(1, 1, 1, 0deg) translateX(0); opacity: 1; }}
            100% {{ transform: translateY(110vh) rotate3d(1, 2, 0.5, 1080deg) translateX(100px); opacity: 0; }}
        }}
        @keyframes fallSpiral {{
            0% {{ transform: translateY(0) rotateY(0deg) translateX(0); opacity: 1; }}
            100% {{ transform: translateY(110vh) rotateY(1440deg) translateX(-150px); opacity: 0; }}
        }}

        /* Rising Flower Bouquet (Upgraded) */
        .bouquet-container {{
            position: fixed;
            bottom: -250px;
            left: 8%;
            z-index: 2;
            pointer-events: none;
            will-change: transform, opacity;
            animation: bouquetRise 9s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite;
        }}

        @keyframes bouquetRise {{
            0% {{ transform: translateY(0) rotate(-3deg); opacity: 0; }}
            8% {{ opacity: 1; }}
            85% {{ opacity: 1; }}
            100% {{ transform: translateY(-110vh) rotate(3deg); opacity: 0; }}
        }}

        .bouquet {{
            position: relative;
            width: 180px;
            height: 250px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
        }}

        /* Stems */
        .stem-bundle {{
            position: absolute;
            bottom: 25px;
            width: 30px;
            height: 120px;
            display: flex;
            justify-content: space-around;
        }}
        .stem-line {{
            width: 3px;
            height: 100%;
            background: #2ecc71;
            transform-origin: bottom;
        }}
        .stem-line:nth-child(1) {{ transform: rotate(-10deg); }}
        .stem-line:nth-child(2) {{ transform: rotate(-3deg); }}
        .stem-line:nth-child(3) {{ transform: rotate(4deg); }}
        .stem-line:nth-child(4) {{ transform: rotate(12deg); }}

        /* Bow */
        .bow {{
            position: absolute;
            bottom: 30px;
            width: 40px;
            height: 20px;
            background: #ff6b9d;
            border-radius: 10px;
            z-index: 5;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            left: 50%;
            transform: translateX(-50%);
        }}
        .bow::before, .bow::after {{
            content: '';
            position: absolute;
            width: 30px;
            height: 25px;
            border: 5px solid #ff6b9d;
            border-radius: 50%;
            top: -10px;
        }}
        .bow::before {{ left: -20px; transform: rotate(-20deg); border-right-color: transparent; }}
        .bow::after {{ right: -20px; transform: rotate(20deg); border-left-color: transparent; }}

        /* Leaves */
        .leaf {{
            position: absolute;
            width: 25px;
            height: 15px;
            background: #2ecc71;
            border-radius: 50% 0 50% 0;
            z-index: 1;
            box-shadow: inset 2px 2px 5px rgba(255,255,255,0.3);
        }}
        .leaf-1 {{ bottom: 120px; left: 30px; transform: rotate(-45deg); }}
        .leaf-2 {{ bottom: 140px; left: 130px; transform: rotate(45deg); }}
        .leaf-3 {{ bottom: 90px; left: 40px; transform: rotate(-20deg); }}
        .leaf-4 {{ bottom: 100px; left: 120px; transform: rotate(20deg); }}
        .leaf-5 {{ bottom: 150px; left: 70px; transform: rotate(-80deg); }}

        /* Flowers */
        .b-flower {{
            position: absolute;
            width: 40px;
            height: 40px;
            z-index: 3;
            transform-origin: center;
            animation: gentleSway infinite alternate;
            will-change: transform;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        @keyframes gentleSway {{
            0% {{ transform: scale(0.95); }}
            100% {{ transform: scale(1.05); }}
        }}

        .b-petal {{
            position: absolute;
            width: 16px;
            height: 40px;
            border-radius: 50%;
            background: var(--c);
            opacity: 0.9;
            box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
        }}
        
        .b-center {{
            position: absolute;
            width: 14px;
            height: 14px;
            background: #fff;
            border-radius: 50%;
            z-index: 2;
            box-shadow: 0 0 5px rgba(0,0,0,0.2);
        }}

        /* Dome arrangement */
        .f1 {{ bottom: 180px; left: 70px; animation-duration: 3.2s; --c: #ff6b9d; }}
        .f2 {{ bottom: 160px; left: 35px; animation-duration: 3.7s; --c: #00d4aa; }}
        .f3 {{ bottom: 165px; left: 105px; animation-duration: 3.4s; --c: #ffd700; }}
        .f4 {{ bottom: 135px; left: 20px; animation-duration: 3.9s; --c: #4CAF50; }}
        .f5 {{ bottom: 140px; left: 65px; animation-duration: 3.1s; --c: #ff4757; }}
        .f6 {{ bottom: 140px; left: 120px; animation-duration: 3.5s; --c: #ff6b9d; }}
        .f7 {{ bottom: 110px; left: 45px; animation-duration: 3.8s; --c: #ffd700; }}
        .f8 {{ bottom: 115px; left: 95px; animation-duration: 3.3s; --c: #00d4aa; }}
        .f9 {{ bottom: 170px; left: 50px; animation-duration: 3.6s; --c: #ff4757; z-index: 4; }}
        .f10 {{ bottom: 155px; left: 85px; animation-duration: 3.2s; --c: #4CAF50; z-index: 4; }}
        
        /* Sparkles */
        .sparkle {{
            position: absolute;
            color: #fff;
            font-size: 16px;
            text-shadow: 0 0 5px #fff;
            animation: sparkleFade 2s infinite;
            will-change: opacity;
        }}
        .s1 {{ bottom: 200px; left: 40px; animation-delay: 0s; }}
        .s2 {{ bottom: 180px; left: 140px; animation-delay: 0.5s; }}
        .s3 {{ bottom: 130px; left: 10px; animation-delay: 1s; }}
        .s4 {{ bottom: 110px; left: 150px; animation-delay: 1.5s; }}
        .s5 {{ bottom: 220px; left: 90px; animation-delay: 0.8s; }}

        @keyframes sparkleFade {{
            0%, 100% {{ opacity: 0; transform: scale(0.5); }}
            50% {{ opacity: 1; transform: scale(1.2); }}
        }}

        @media (max-width: 768px) {{
            .bouquet-container {{
                left: auto;
                right: 8%;
            }}
            .love-message {{
                font-size: 1.1em;
            }}
            /* Hide some flowers for performance on mobile */
            .f8, .f9, .f10, .s4, .s5 {{ display: none; }}
        }}
    </style>
</head>
<body>
    <!-- Upgraded Rising Flower Bouquet -->
    <div class="bouquet-container">
        <div class="bouquet">
            <div class="stem-bundle">
                <div class="stem-line"></div><div class="stem-line"></div>
                <div class="stem-line"></div><div class="stem-line"></div>
            </div>
            <div class="bow"></div>
            
            <div class="leaf leaf-1"></div>
            <div class="leaf leaf-2"></div>
            <div class="leaf leaf-3"></div>
            <div class="leaf leaf-4"></div>
            <div class="leaf leaf-5"></div>

            <!-- Flowers 1 to 10 -->
            <div class="b-flower f1"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f2"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f3"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f4"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f5"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f6"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f7"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f8"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f9"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            <div class="b-flower f10"><div class="b-petal" style="transform:rotate(0deg)"></div><div class="b-petal" style="transform:rotate(60deg)"></div><div class="b-petal" style="transform:rotate(120deg)"></div><div class="b-center"></div></div>
            
            <!-- Sparkles -->
            <div class="sparkle s1">✦</div>
            <div class="sparkle s2">✦</div>
            <div class="sparkle s3">✦</div>
            <div class="sparkle s4">✦</div>
            <div class="sparkle s5">✦</div>
        </div>
    </div>

    <div class="container">
        <!-- Photo Reveal Section -->
        <div class="photo-reveal" id="photoReveal">
            <img src="data:image/jpeg;base64,{b64_str}" alt="Aile fotoğrafı" />
            <p class="love-message">Oğlun seni çok seviyor annem, anneler günün kutlu olsun 💕</p>
        </div>

        <h1 class="fade-in-up">Anneler Günü Kutlaması <span class="heart-icon pulse">❤️</span></h1>
        <p class="subtitle fade-in-up">Sana çok sevgi dolu günler diliyorum</p>

        <div class="love-bar-container fade-in-up">
            <div class="love-bar-label">
                <span>Sevgi Seviyesi <span class="heart-icon pulse" id="love-heart">💕</span></span>
                <span class="love-pct">0%</span>
            </div>
            <div class="love-bar">
                <div class="love-fill"></div>
            </div>
        </div>

        <button class="confetti-button fade-in-up" onclick="createConfetti()">Konfeti Patlat! 🎉</button>
    </div>

    <script>
        // Background particles generator
        const particleCount = 25; // reduced for perf
        const body = document.body;
        for(let i = 0; i < particleCount; i++) {{
            const p = document.createElement('div');
            p.className = 'bg-particle';
            p.style.left = Math.random() * 100 + 'vw';
            const size = Math.random() * 3 + 2;
            p.style.width = size + 'px';
            p.style.height = size + 'px';
            p.style.animationDuration = (Math.random() * 10 + 8) + 's';
            p.style.animationDelay = (Math.random() * 5) + 's';
            body.appendChild(p);
        }}

        // Advanced Confetti
        function createConfetti() {{
            const colors = ['#ff6b9d', '#ff8fab', '#ffa5c0', '#00d4aa', '#ffd700', '#4CAF50', '#a29bfe'];
            const confettiCount = 100; // slightly reduced for mobile perf
            
            // Audio effect for burst
            try {{
                const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const oscillator = audioCtx.createOscillator();
                const gainNode = audioCtx.createGain();
                oscillator.type = 'triangle';
                oscillator.frequency.setValueAtTime(400, audioCtx.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(800, audioCtx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
                oscillator.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                oscillator.start();
                oscillator.stop(audioCtx.currentTime + 0.5);
            }} catch(e) {{
                console.log("Audio not supported or disabled");
            }}

            for (let i = 0; i < confettiCount; i++) {{
                const confetti = document.createElement('div');
                confetti.className = 'adv-confetti';
                
                const size = Math.random() * 10 + 5;
                const isCircle = Math.random() > 0.5;
                
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.width = size + 'px';
                confetti.style.height = (isCircle ? size : size * 2) + 'px';
                confetti.style.borderRadius = isCircle ? '50%' : '2px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                
                const animType = Math.random() > 0.5 ? 'fallTumble' : 'fallSpiral';
                const duration = Math.random() * 3 + 2;
                
                confetti.style.animation = `\${{animType}} \${{duration}}s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards`;
                confetti.style.animationDelay = (Math.random() * 0.2) + 's';
                
                document.body.appendChild(confetti);

                // Cleanup
                setTimeout(() => confetti.remove(), (duration + 1) * 1000);
            }}

            // Reveal photo
            const photoReveal = document.getElementById('photoReveal');
            photoReveal.classList.add('visible');
        }}

        // On Load Animations
        window.addEventListener('load', () => {{
            // Love Bar Animation
            setTimeout(() => {{
                const fill = document.querySelector('.love-fill');
                const pctSpan = document.querySelector('.love-pct');
                const heart = document.getElementById('love-heart');
                
                let start = null;
                const duration = 2500;
                
                function animateFill(timestamp) {{
                    if (!start) start = timestamp;
                    const progress = Math.min((timestamp - start) / duration, 1);
                    
                    const ease = 1 - Math.pow(1 - progress, 4);
                    const currentPct = Math.floor(ease * 100);
                    
                    fill.style.width = currentPct + '%';
                    pctSpan.textContent = currentPct + '%';
                    
                    if (progress < 1) {{
                        requestAnimationFrame(animateFill);
                    }} else {{
                        heart.classList.remove('pulse');
                        heart.classList.add('fast-beat');
                    }}
                }}
                requestAnimationFrame(animateFill);
            }}, 1500);
        }});
    </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
