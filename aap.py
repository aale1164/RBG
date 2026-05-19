<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>AI PowerPoint Generator | Futuristic SaaS</title>
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 (Free) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <!-- AOS CSS -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="animated-bg"></div>
  <nav class="glass-nav">
    <div class="nav-container">
      <div class="logo">
        <i class="fas fa-brain"></i>
        <span>SlideAI</span>
      </div>
      <ul class="nav-links" id="navLinks">
        <li><a href="index.html" class="active">Home</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#templates">Templates</a></li>
        <li><a href="pricing.html">Pricing</a></li>
        <li><a href="dashboard.html">Dashboard</a></li>
      </ul>
      <div class="nav-buttons">
        <a href="login.html" class="btn-outline">Sign In</a>
        <a href="generate.html" class="btn-primary">Start Free</a>
      </div>
      <div class="menu-icon" id="menuIcon">
        <i class="fas fa-bars"></i>
      </div>
    </div>
  </nav>

  <main>
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content" data-aos="fade-up" data-aos-duration="1000">
        <div class="hero-badge glow">
          <i class="fas fa-magic"></i> AI-Powered Presentations
        </div>
        <h1 class="hero-title">Create Professional <span class="gradient-text">AI Presentations</span> in Seconds</h1>
        <p class="hero-desc">Revolutionize your workflow — generate stunning slides with our cutting-edge AI. Trusted by startups and Fortune 500s.</p>
        <div class="hero-buttons">
          <a href="generate.html" class="btn-primary btn-large"><i class="fas fa-bolt"></i> Start Free</a>
          <a href="#" class="btn-outline btn-large" id="watchDemoBtn"><i class="fas fa-play"></i> Watch Demo</a>
        </div>
      </div>
      <div class="hero-stats" data-aos="fade-up" data-aos-delay="200">
        <div><span>10k+</span> Presentations Created</div>
        <div><span>4.9</span> <i class="fas fa-star"></i> User Rating</div>
        <div><span>AI</span> GPT-4 Engine</div>
      </div>
    </section>

    <!-- AI Generator Form (Quick Demo) -->
    <section class="generator-form-section" data-aos="fade-up">
      <div class="glass-card gradient-border">
        <h2>✨ Try AI Presentation Generator</h2>
        <p>Enter a topic and we'll generate a complete deck</p>
        <form id="quickGenForm">
          <div class="form-row">
            <input type="text" id="quickTopic" placeholder="e.g., Future of Quantum Computing" required>
            <select id="quickSlides">
              <option value="5">5 Slides</option>
              <option value="8">8 Slides</option>
              <option value="12">12 Slides</option>
            </select>
            <button type="submit" class="btn-primary">Generate <i class="fas fa-arrow-right"></i></button>
          </div>
        </form>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
      <div class="section-header" data-aos="fade-up">
        <h2>Powerful <span class="gradient-text">AI Features</span></h2>
        <p>Everything you need to create compelling presentations in minutes</p>
      </div>
      <div class="features-grid">
        <div class="feature-card glass-card" data-aos="zoom-in">
          <i class="fas fa-robot"></i>
          <h3>Intelligent Content</h3>
          <p>Generates structured slides, bullet points & speaker notes from any topic.</p>
        </div>
        <div class="feature-card glass-card" data-aos="zoom-in" data-aos-delay="100">
          <i class="fas fa-palette"></i>
          <h3>Smart Design</h3>
          <p>Auto-layout, color harmony and professional templates tailored to your brand.</p>
        </div>
        <div class="feature-card glass-card" data-aos="zoom-in" data-aos-delay="200">
          <i class="fas fa-chart-line"></i>
          <h3>Data Visualization</h3>
          <p>AI charts, graphs and infographics from raw data in seconds.</p>
        </div>
        <div class="feature-card glass-card" data-aos="zoom-in" data-aos-delay="300">
          <i class="fas fa-language"></i>
          <h3>Multilingual AI</h3>
          <p>Supports 50+ languages — global ready presentations.</p>
        </div>
      </div>
    </section>

    <!-- Templates Section -->
    <section id="templates" class="templates">
      <div class="section-header" data-aos="fade-up">
        <h2>Stunning <span class="gradient-text">Templates</span></h2>
        <p>Choose from 200+ AI-optimized slide decks</p>
      </div>
      <div class="templates-slider" id="templatesGrid">
        <!-- JS injects dynamic template cards, but also static fallback -->
      </div>
    </section>

    <!-- Pricing Section -->
    <section class="pricing" id="pricing">
      <div class="section-header" data-aos="fade-up">
        <h2>Simple, <span class="gradient-text">Transparent</span> Pricing</h2>
        <p>Scale as you grow. No hidden fees.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card glass-card" data-aos="flip-left">
          <div class="plan-name">Starter</div>
          <div class="price">$0<span>/month</span></div>
          <ul>
            <li><i class="fas fa-check"></i> 10 AI presentations/month</li>
            <li><i class="fas fa-check"></i> Basic templates</li>
            <li><i class="fas fa-check"></i> Export to PPTX/PDF</li>
            <li><i class="fas fa-times"></i> Premium support</li>
          </ul>
          <a href="generate.html" class="btn-outline">Get Started</a>
        </div>
        <div class="pricing-card glass-card premium" data-aos="flip-left" data-aos-delay="100">
          <div class="popular-badge">Most Popular</div>
          <div class="plan-name">Pro</div>
          <div class="price">$19<span>/month</span></div>
          <ul>
            <li><i class="fas fa-check"></i> Unlimited presentations</li>
            <li><i class="fas fa-check"></i> All templates + AI style</li>
            <li><i class="fas fa-check"></i> Custom brand kit</li>
            <li><i class="fas fa-check"></i> Priority support</li>
          </ul>
          <a href="login.html" class="btn-primary">Start Pro</a>
        </div>
        <div class="pricing-card glass-card" data-aos="flip-left" data-aos-delay="200">
          <div class="plan-name">Enterprise</div>
          <div class="price">Custom</div>
          <ul>
            <li><i class="fas fa-check"></i> SSO & compliance</li>
            <li><i class="fas fa-check"></i> Dedicated AI instance</li>
            <li><i class="fas fa-check"></i> API access</li>
            <li><i class="fas fa-check"></i> 24/7 enterprise support</li>
          </ul>
          <a href="#" class="btn-outline">Contact Sales</a>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials">
      <div class="section-header" data-aos="fade-up">
        <h2>Loved by <span class="gradient-text">creators</span> worldwide</h2>
      </div>
      <div class="testimonial-grid">
        <div class="testimonial-card glass-card" data-aos="fade-right">
          <i class="fas fa-quote-left"></i>
          <p>"SlideAI cut our deck creation time by 80%. The AI's storytelling is genuinely impressive."</p>
          <div class="user"><img src="https://randomuser.me/api/portraits/women/68.jpg" alt="avatar"><span>— Sarah Chen, Product Lead @ ScaleUp</span></div>
        </div>
        <div class="testimonial-card glass-card" data-aos="fade-up">
          <i class="fas fa-quote-left"></i>
          <p>"The design quality rivals top agencies. A must-have for modern startups."</p>
          <div class="user"><img src="https://randomuser.me/api/portraits/men/32.jpg" alt="avatar"><span>— Marcus V., CMO at Nexify</span></div>
        </div>
        <div class="testimonial-card glass-card" data-aos="fade-left">
          <i class="fas fa-quote-left"></i>
          <p>"Finally an AI that understands slide narrative. Game changer."</p>
          <div class="user"><img src="https://randomuser.me/api/portraits/women/45.jpg" alt="avatar"><span>— Dr. Emily Zhou, Education</span></div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq">
      <div class="section-header" data-aos="fade-up">
        <h2>Frequently Asked <span class="gradient-text">Questions</span></h2>
      </div>
      <div class="faq-grid">
        <div class="faq-item glass-card" data-aos="fade-up">
          <div class="faq-question">How does the AI generate slides? <i class="fas fa-chevron-down"></i></div>
          <div class="faq-answer">Our AI analyzes your topic, retrieves relevant data, and builds structured narratives with visual suggestions. Powered by GPT-4 and proprietary design models.</div>
        </div>
        <div class="faq-item glass-card" data-aos="fade-up" data-aos-delay="100">
          <div class="faq-question">Can I export to PowerPoint? <i class="fas fa-chevron-down"></i></div>
          <div class="faq-answer">Yes, export as PPTX, PDF, or Google Slides. Fully editable.</div>
        </div>
        <div class="faq-item glass-card" data-aos="fade-up" data-aos-delay="200">
          <div class="faq-question">Is there a free trial? <i class="fas fa-chevron-down"></i></div>
          <div class="faq-answer">Absolutely! The Starter plan includes 10 free presentations with full features.</div>
        </div>
        <div class="faq-item glass-card" data-aos="fade-up" data-aos-delay="300">
          <div class="faq-question">Can I use custom brand colors? <i class="fas fa-chevron-down"></i></div>
          <div class="faq-answer">Pro and Enterprise plans include brand kits and custom theming.</div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col">
        <div class="logo"><i class="fas fa-brain"></i> SlideAI</div>
        <p>AI presentation generator that redefines productivity.</p>
        <div class="socials">
          <a href="#"><i class="fab fa-twitter"></i></a>
          <a href="#"><i class="fab fa-linkedin"></i></a>
          <a href="#"><i class="fab fa-github"></i></a>
        </div>
      </div>
      <div class="footer-col"><h4>Product</h4><a href="#">Pricing</a><a href="#">Templates</a><a href="#">Enterprise</a></div>
      <div class="footer-col"><h4>Resources</h4><a href="#">Blog</a><a href="#">Docs</a><a href="#">Support</a></div>
      <div class="footer-col"><h4>Company</h4><a href="#">About</a><a href="#">Careers</a><a href="#">Legal</a></div>
    </div>
    <div class="footer-bottom">© 2025 SlideAI — The future of presentations.</div>
  </footer>

  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="js/app.js"></script>
  <script>
    // Template data render
    const templatesList = [
      "Business", "Education", "Technology", "Cyber Security", "Marketing", "Startup Pitch", "AI Presentation"
    ];
    const grid = document.getElementById('templatesGrid');
    if(grid){
      grid.innerHTML = templatesList.map(t => `<div class="template-card glass-card" data-aos="fade-up"><i class="fas fa-slideshare"></i><h4>${t}</h4><p>Modern ${t.toLowerCase()} deck</p><div class="template-glow"></div></div>`).join('');
    }
    // Quick generator redirect to generate page with params
    const quickForm = document.getElementById('quickGenForm');
    if(quickForm){
      quickForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const topic = document.getElementById('quickTopic').value;
        const slides = document.getElementById('quickSlides').value;
        window.location.href = `generate.html?topic=${encodeURIComponent(topic)}&slides=${slides}`;
      });
    }
    // FAQ toggle
    document.querySelectorAll('.faq-question').forEach(q => {
      q.addEventListener('click', () => {
        const parent = q.parentElement;
        parent.classList.toggle('active');
      });
    });
    // Watch Demo alert
    document.getElementById('watchDemoBtn')?.addEventListener('click', (e) => {
      e.preventDefault();
      alert("🎥 Demo video: watch how SlideAI creates pro slides in seconds! (Full interactive preview coming soon)");
    });
  </script>
</body>
</html>
