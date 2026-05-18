<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title>خدمة المواطن | Citizen Services</title>
  <!-- Google Fonts: Tajawal & Cairo for Arabic, Inter for English -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=El+Messiri:wght@500;700&family=Inter:wght@400;500;600;700&family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    /* ========== CSS Variables ========== */
    :root {
      --primary: #0a192f;
      --secondary: #112240;
      --accent: #d4a017;
      --gold: #f0c040;
      --text: #e6f1ff;
      --text-muted: #8892b0;
      --border: #1e3a5f;
      --font-ar: 'Tajawal', 'Cairo', 'El Messiri', sans-serif;
      --font-en: 'Inter', sans-serif;
      --sidebar-width: 280px;
      --transition: all 0.3s ease;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-ar);
      background-color: var(--primary);
      color: var(--text);
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* ========== Sidebar ========== */
    .sidebar {
      width: var(--sidebar-width);
      background: var(--secondary);
      border-left: 2px solid var(--gold);
      box-shadow: 4px 0 20px rgba(0,0,0,0.5);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      right: 0;
      height: 100vh;
      z-index: 100;
      transition: var(--transition);
      overflow-y: auto;
    }

    .sidebar-header {
      padding: 20px;
      text-align: center;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(135deg, #0a192f, #1e3a5f);
    }

    .sidebar-header .logo-icon {
      font-size: 3rem;
      color: var(--gold);
      margin-bottom: 5px;
    }

    .sidebar-header h2 {
      font-family: 'El Messiri', sans-serif;
      font-size: 1.6rem;
      color: var(--gold);
      letter-spacing: 1px;
      margin: 0;
    }

    .sidebar-header p {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 5px;
    }

    .sidebar-nav {
      flex: 1;
      padding: 15px 0;
    }

    .sidebar-nav .category-title {
      padding: 12px 20px 5px;
      font-size: 0.75rem;
      text-transform: uppercase;
      color: var(--accent);
      letter-spacing: 1px;
      font-weight: 700;
      opacity: 0.8;
    }

    .sidebar-nav a {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 20px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      transition: var(--transition);
      border-right: 3px solid transparent;
      margin: 2px 0;
    }

    .sidebar-nav a i {
      width: 24px;
      font-size: 1.2rem;
      text-align: center;
      color: var(--accent);
    }

    .sidebar-nav a:hover,
    .sidebar-nav a.active {
      background: rgba(212, 160, 23, 0.1);
      color: var(--gold);
      border-right-color: var(--gold);
      font-weight: 500;
    }

    .sidebar-footer {
      padding: 15px;
      border-top: 1px solid var(--border);
      text-align: center;
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    /* ========== Main Content ========== */
    .main-content {
      margin-right: var(--sidebar-width);
      flex: 1;
      padding: 25px;
      position: relative;
      z-index: 1;
    }

    .top-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
      background: var(--secondary);
      padding: 15px 25px;
      border-radius: 16px;
      border: 1px solid var(--border);
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }

    .top-header .header-left h1 {
      font-family: 'El Messiri', sans-serif;
      font-size: 1.8rem;
      color: var(--gold);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .x-link {
      display: flex;
      align-items: center;
      gap: 8px;
      background: #000;
      color: #fff;
      padding: 10px 18px;
      border-radius: 30px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.9rem;
      transition: var(--transition);
      border: 1px solid #333;
    }

    .x-link:hover {
      background: #1a1a1a;
      border-color: var(--gold);
      transform: translateY(-2px);
    }

    .lang-switch {
      background: var(--primary);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 8px 15px;
      border-radius: 30px;
      cursor: pointer;
      font-family: var(--font-en);
      transition: var(--transition);
    }

    .lang-switch:hover {
      border-color: var(--gold);
    }

    .tool-container {
      background: var(--secondary);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 30px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      min-height: 500px;
    }

    .tool-header {
      border-bottom: 2px solid var(--border);
      padding-bottom: 15px;
      margin-bottom: 25px;
      display: flex;
      align-items: center;
      gap: 15px;
    }

    .tool-header i {
      font-size: 2.2rem;
      color: var(--gold);
    }

    .tool-header h2 {
      font-family: 'El Messiri', sans-serif;
      font-size: 1.8rem;
      color: var(--text);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--gold), #b8860b);
      color: #000;
      border: none;
      padding: 12px 28px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(212,160,23,0.3);
    }

    input, textarea, select {
      background: var(--primary);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 12px 16px;
      border-radius: 12px;
      font-family: inherit;
      width: 100%;
      margin: 10px 0;
    }

    .row {
      display: flex;
      gap: 20px;
      flex-wrap: wrap;
    }

    @media (max-width: 768px) {
      .sidebar {
        transform: translateX(100%);
        width: 260px;
      }
      .sidebar.open {
        transform: translateX(0);
      }
      .main-content {
        margin-right: 0;
      }
      .menu-toggle {
        display: block;
        background: var(--accent);
        border: none;
        color: #000;
        font-size: 1.5rem;
        border-radius: 8px;
        padding: 5px 10px;
        cursor: pointer;
      }
    }
  </style>
</head>
<body>
  <!-- ========== Sidebar ========== -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="logo-icon"><i class="fas fa-shield-alt"></i></div>
      <h2>خدمة المواطن</h2>
      <p>بوابتك الإلكترونية الشاملة</p>
    </div>
    <nav class="sidebar-nav">
      <div class="category-title" data-lang="main-tools">الأدوات الرئيسية</div>
      <a href="#" data-tool="dashboard" class="active"><i class="fas fa-th-large"></i> <span data-lang="dashboard">لوحة التحكم</span></a>
      <a href="#" data-tool="image-video-analyzer"><i class="fas fa-search"></i> <span data-lang="analyzer">محلل الصور والفيديو</span></a>
      <a href="#" data-tool="cv-builder"><i class="fas fa-file-alt"></i> <span data-lang="cv">منشئ السيرة الذاتية</span></a>
      <a href="#" data-tool="id-photo"><i class="fas fa-id-card"></i> <span data-lang="id-photo">معالج صورة الهوية</span></a>
      <a href="#" data-tool="img-to-pdf"><i class="fas fa-file-pdf"></i> <span data-lang="img2pdf">صور إلى PDF</span></a>
      <div class="category-title" data-lang="dev-tools">أدوات المطورين</div>
      <a href="#" data-tool="code-playground"><i class="fas fa-code"></i> <span data-lang="code-playground">محرر الأكواد</span></a>
      <a href="#" data-tool="http-profiler"><i class="fas fa-network-wired"></i> <span data-lang="http-profiler">محلل الطلبات</span></a>
      <a href="#" data-tool="key-generator"><i class="fas fa-key"></i> <span data-lang="key-gen">مولد مفاتيح التشفير</span></a>
      <a href="#" data-tool="system-monitor"><i class="fas fa-microchip"></i> <span data-lang="sys-monitor">مراقب النظام</span></a>
      <a href="#" data-tool="json-formatter"><i class="fas fa-code"></i> <span data-lang="json-formatter">JSON Formatter</span></a>
      <div class="category-title" data-lang="media-tools">الوسائط والصوتيات</div>
      <a href="#" data-tool="compressor"><i class="fas fa-compress"></i> <span data-lang="compressor">ضاغط الوسائط</span></a>
      <a href="#" data-tool="bg-remover"><i class="fas fa-eraser"></i> <span data-lang="bg-remover">مزيل الخلفية</span></a>
      <a href="#" data-tool="text-to-speech"><i class="fas fa-volume-up"></i> <span data-lang="tts">نص إلى كلام</span></a>
      <a href="#" data-tool="pdf-editor"><i class="fas fa-pencil-alt"></i> <span data-lang="pdf-editor">محرر PDF</span></a>
      <div class="category-title" data-lang="video-tools">فيديو متقدم</div>
      <a href="#" data-tool="video-translator"><i class="fas fa-language"></i> <span data-lang="video-translator">مترجم الفيديو</span></a>
      <a href="#" data-tool="photo-video-maker"><i class="fas fa-film"></i> <span data-lang="photo-video">صانع فيديو من الصور</span></a>
      <a href="#" data-tool="subtitle-editor"><i class="fas fa-closed-captioning"></i> <span data-lang="subtitle-editor">محرر الترجمة</span></a>
      <a href="#" data-tool="dubbing"><i class="fas fa-microphone-alt"></i> <span data-lang="dubbing">مدبلج الفيديو</span></a>
      <div class="category-title" data-lang="account-tools">الحساب والأمان</div>
      <a href="#" data-tool="auth-security"><i class="fas fa-shield-haltered"></i> <span data-lang="auth">المصادقة والأمان</span></a>
      <a href="#" data-tool="file-converter"><i class="fas fa-exchange-alt"></i> <span data-lang="file-converter">محول الملفات</span></a>
    </nav>
    <div class="sidebar-footer">© 2026 Citizen Services</div>
  </aside>

  <!-- ========== Main Content ========== -->
  <main class="main-content" id="mainContent">
    <header class="top-header">
      <div class="header-left">
        <button class="menu-toggle" id="menuToggle" style="display:none;"><i class="fas fa-bars"></i></button>
        <h1>خدمة المواطن</h1>
      </div>
      <div class="header-right">
        <a href="https://x.com/aale1164" target="_blank" class="x-link" rel="noopener">
          <i class="fab fa-x-twitter"></i> @aale1164
        </a>
        <button class="lang-switch" id="langSwitch">English</button>
      </div>
    </header>
    <div id="toolContainer" class="tool-container"></div>
  </main>

  <script>
    (function() {
      // ========== Multi-language support ==========
      const translations = {
        ar: {
          'dashboard': 'لوحة التحكم',
          'analyzer': 'محلل الصور والفيديو',
          'cv': 'منشئ السيرة الذاتية',
          'id-photo': 'معالج صورة الهوية',
          'img2pdf': 'صور إلى PDF',
          'code-playground': 'محرر الأكواد',
          'http-profiler': 'محلل طلبات HTTP',
          'key-gen': 'مولد مفاتيح التشفير',
          'sys-monitor': 'مراقب النظام',
          'json-formatter': 'JSON Formatter',
          'compressor': 'ضاغط الوسائط',
          'bg-remover': 'مزيل الخلفية',
          'tts': 'نص إلى كلام',
          'pdf-editor': 'محرر PDF',
          'video-translator': 'مترجم الفيديو',
          'photo-video': 'صانع فيديو من الصور',
          'subtitle-editor': 'محرر الترجمة',
          'dubbing': 'مدبلج الفيديو',
          'auth': 'المصادقة والأمان',
          'file-converter': 'محول الملفات'
        },
        en: {
          'dashboard': 'Dashboard',
          'analyzer': 'Image & Video Analyzer',
          'cv': 'CV Builder',
          'id-photo': 'ID Photo Processor',
          'img2pdf': 'Images to PDF',
          'code-playground': 'Code Playground',
          'http-profiler': 'HTTP Profiler',
          'key-gen': 'Key Generator',
          'sys-monitor': 'System Monitor',
          'json-formatter': 'JSON Formatter',
          'compressor': 'Media Compressor',
          'bg-remover': 'Background Remover',
          'tts': 'Text to Speech',
          'pdf-editor': 'PDF Editor',
          'video-translator': 'Video Translator',
          'photo-video': 'Photo Video Maker',
          'subtitle-editor': 'Subtitle Editor',
          'dubbing': 'Video Dubbing',
          'auth': 'Authentication & Security',
          'file-converter': 'File Converter'
        }
      };

      let currentLang = 'ar';

      // ========== Tool definitions ==========
      const tools = {
        dashboard: {
          icon: 'fa-th-large',
          title: { ar: 'لوحة التحكم', en: 'Dashboard' },
          content: {
            ar: `<p>مرحباً بك في منصة خدمات المواطن. اختر الأداة من الشريط الجانبي.</p>`,
            en: `<p>Welcome to Citizen Services Platform. Select a tool from the sidebar.</p>`
          }
        },
        'image-video-analyzer': {
          icon: 'fa-search',
          title: { ar: 'محلل الصور والفيديو', en: 'Image & Video Analyzer' },
          content: {
            ar: `<input type="file" accept="image/*,video/*"><button class="btn-primary"><i class="fas fa-microscope"></i> بدء التحليل</button>`,
            en: `<input type="file" accept="image/*,video/*"><button class="btn-primary"><i class="fas fa-microscope"></i> Start Analysis</button>`
          }
        },
        'cv-builder': {
          icon: 'fa-file-alt',
          title: { ar: 'منشئ السيرة الذاتية', en: 'CV Builder' },
          content: {
            ar: `<input placeholder="الاسم الكامل"><button class="btn-primary"><i class="fas fa-magic"></i> إنشاء السيرة الذاتية</button>`,
            en: `<input placeholder="Full Name"><button class="btn-primary"><i class="fas fa-magic"></i> Generate CV</button>`
          }
        },
        'id-photo': {
          icon: 'fa-id-card',
          title: { ar: 'معالج صورة الهوية', en: 'ID Photo Processor' },
          content: {
            ar: `<select><option>هوية وطنية سعودية</option><option>جواز سفر</option></select><input type="file" accept="image/*"><button class="btn-primary"><i class="fas fa-crop"></i> تجهيز الصورة</button>`,
            en: `<select><option>Saudi National ID</option><option>Passport</option></select><input type="file" accept="image/*"><button class="btn-primary"><i class="fas fa-crop"></i> Process Photo</button>`
          }
        },
        'img-to-pdf': {
          icon: 'fa-file-pdf',
          title: { ar: 'صور إلى PDF', en: 'Images to PDF' },
          content: {
            ar: `<input type="file" accept="image/*" multiple><button class="btn-primary"><i class="fas fa-file-export"></i> تحويل إلى PDF</button>`,
            en: `<input type="file" accept="image/*" multiple><button class="btn-primary"><i class="fas fa-file-export"></i> Convert to PDF</button>`
          }
        },
        'code-playground': {
          icon: 'fa-code',
          title: { ar: 'محرر الأكواد', en: 'Code Playground' },
          content: {
            ar: `<textarea placeholder="أكتب الكود هنا..." style="height:200px; direction:ltr;"></textarea><button class="btn-primary"><i class="fas fa-play"></i> تشغيل</button>`,
            en: `<textarea placeholder="Write your code here..." style="height:200px; direction:ltr;"></textarea><button class="btn-primary"><i class="fas fa-play"></i> Run</button>`
          }
        },
        'http-profiler': {
          icon: 'fa-network-wired',
          title: { ar: 'محلل طلبات HTTP', en: 'HTTP Profiler' },
          content: {
            ar: `<input placeholder="https://api.example.com" style="direction:ltr;"><button class="btn-primary"><i class="fas fa-paper-plane"></i> إرسال</button>`,
            en: `<input placeholder="https://api.example.com" style="direction:ltr;"><button class="btn-primary"><i class="fas fa-paper-plane"></i> Send</button>`
          }
        },
        'key-generator': {
          icon: 'fa-key',
          title: { ar: 'مولد مفاتيح التشفير', en: 'Key Generator' },
          content: {
            ar: `<select><option>RSA 2048</option><option>AES 256</option></select><button class="btn-primary"><i class="fas fa-sync-alt"></i> توليد</button>`,
            en: `<select><option>RSA 2048</option><option>AES 256</option></select><button class="btn-primary"><i class="fas fa-sync-alt"></i> Generate</button>`
          }
        },
        'system-monitor': {
          icon: 'fa-microchip',
          title: { ar: 'مراقب النظام', en: 'System Monitor' },
          content: {
            ar: `<div id="systemStats"><i class="fas fa-spinner fa-pulse"></i> جاري تحميل بيانات النظام...</div>`,
            en: `<div id="systemStats"><i class="fas fa-spinner fa-pulse"></i> Loading system data...</div>`
          }
        },
        'json-formatter': {
          icon: 'fa-code',
          title: { ar: 'JSON Formatter', en: 'JSON Formatter' },
          content: {
            ar: `<textarea placeholder="الصق كود JSON هنا..." style="direction:ltr;"></textarea><button class="btn-primary"><i class="fas fa-magic"></i> تنسيق</button>`,
            en: `<textarea placeholder="Paste JSON here..." style="direction:ltr;"></textarea><button class="btn-primary"><i class="fas fa-magic"></i> Format</button>`
          }
        },
        'compressor': {
          icon: 'fa-compress',
          title: { ar: 'ضاغط الوسائط', en: 'Media Compressor' },
          content: {
            ar: `<input type="file" accept="image/*,video/*"><button class="btn-primary"><i class="fas fa-compress-arrows-alt"></i> ضغط</button>`,
            en: `<input type="file" accept="image/*,video/*"><button class="btn-primary"><i class="fas fa-compress-arrows-alt"></i> Compress</button>`
          }
        },
        'bg-remover': {
          icon: 'fa-eraser',
          title: { ar: 'مزيل الخلفية', en: 'Background Remover' },
          content: {
            ar: `<input type="file" accept="image/*"><button class="btn-primary"><i class="fas fa-cut"></i> إزالة الخلفية</button>`,
            en: `<input type="file" accept="image/*"><button class="btn-primary"><i class="fas fa-cut"></i> Remove Background</button>`
          }
        },
        'text-to-speech': {
          icon: 'fa-volume-up',
          title: { ar: 'نص إلى كلام', en: 'Text to Speech' },
          content: {
            ar: `<textarea placeholder="أدخل النص هنا..."></textarea><select><option>صوت عربي (ذكر)</option><option>صوت عربي (أنثى)</option></select><button class="btn-primary"><i class="fas fa-play"></i> استماع</button>`,
            en: `<textarea placeholder="Enter text here..."></textarea><select><option>Arabic Male Voice</option><option>Arabic Female Voice</option></select><button class="btn-primary"><i class="fas fa-play"></i> Listen</button>`
          }
        },
        'pdf-editor': {
          icon: 'fa-pencil-alt',
          title: { ar: 'محرر PDF', en: 'PDF Editor' },
          content: {
            ar: `<input type="file" accept=".pdf"><button class="btn-primary"><i class="fas fa-object-group"></i> دمج</button><button class="btn-primary"><i class="fas fa-cut"></i> تقسيم</button>`,
            en: `<input type="file" accept=".pdf"><button class="btn-primary"><i class="fas fa-object-group"></i> Merge</button><button class="btn-primary"><i class="fas fa-cut"></i> Split</button>`
          }
        },
        'video-translator': {
          icon: 'fa-language',
          title: { ar: 'مترجم الفيديو', en: 'Video Translator' },
          content: {
            ar: `<input type="file" accept="video/*"><button class="btn-primary"><i class="fas fa-cc"></i> استخراج الترجمة</button>`,
            en: `<input type="file" accept="video/*"><button class="btn-primary"><i class="fas fa-cc"></i> Extract Subtitles</button>`
          }
        },
        'photo-video-maker': {
          icon: 'fa-film',
          title: { ar: 'صانع الفيديو', en: 'Photo Video Maker' },
          content: {
            ar: `<input type="file" accept="image/*" multiple><button class="btn-primary"><i class="fas fa-video"></i> إنشاء فيديو</button>`,
            en: `<input type="file" accept="image/*" multiple><button class="btn-primary"><i class="fas fa-video"></i> Create Video</button>`
          }
        },
        'subtitle-editor': {
          icon: 'fa-closed-captioning',
          title: { ar: 'محرر الترجمة', en: 'Subtitle Editor' },
          content: {
            ar: `<input type="file" accept="video/*"><textarea placeholder="ملف الترجمة SRT"></textarea><button class="btn-primary"><i class="fas fa-save"></i> حفظ</button>`,
            en: `<input type="file" accept="video/*"><textarea placeholder="SRT Subtitle File"></textarea><button class="btn-primary"><i class="fas fa-save"></i> Save</button>`
          }
        },
        'dubbing': {
          icon: 'fa-microphone-alt',
          title: { ar: 'مدبلج الفيديو', en: 'Video Dubbing' },
          content: {
            ar: `<input type="file" accept="video/*"><select><option>الإنجليزية</option><option>الفرنسية</option></select><button class="btn-primary"><i class="fas fa-microphone"></i> بدء الدبلجة</button>`,
            en: `<input type="file" accept="video/*"><select><option>English</option><option>French</option></select><button class="btn-primary"><i class="fas fa-microphone"></i> Start Dubbing</button>`
          }
        },
        'auth-security': {
          icon: 'fa-shield-haltered',
          title: { ar: 'المصادقة والأمان', en: 'Authentication & Security' },
          content: {
            ar: `<h3>إعدادات الحماية</h3><label>تفعيل المصادقة الثنائية</label><input type="checkbox"><button class="btn-primary"><i class="fas fa-history"></i> سجل النشاطات</button>`,
            en: `<h3>Security Settings</h3><label>Enable Two-Factor Authentication</label><input type="checkbox"><button class="btn-primary"><i class="fas fa-history"></i> Activity Log</button>`
          }
        },
        'file-converter': {
          icon: 'fa-exchange-alt',
          title: { ar: 'محول الملفات', en: 'File Converter' },
          content: {
            ar: `<input type="file"><select><option>PDF إلى Word</option><option>Word إلى PDF</option></select><button class="btn-primary"><i class="fas fa-sync-alt"></i> تحويل</button>`,
            en: `<input type="file"><select><option>PDF to Word</option><option>Word to PDF</option></select><button class="btn-primary"><i class="fas fa-sync-alt"></i> Convert</button>`
          }
        }
      };

      // ========== DOM Elements ==========
      const toolContainer = document.getElementById('toolContainer');
      const sidebarLinks = document.querySelectorAll('.sidebar-nav a[data-tool]');
      const menuToggle = document.getElementById('menuToggle');
      const sidebar = document.getElementById('sidebar');
      const langSwitch = document.getElementById('langSwitch');

      // ========== Functions ==========
      function loadTool(toolId) {
        const tool = tools[toolId];
        if (!tool) return;
        const title = tool.title[currentLang];
        const content = tool.content[currentLang];
        const html = `
          <div class="tool-header">
            <i class="fas ${tool.icon}"></i>
            <h2>${title}</h2>
          </div>
          <div>${content}</div>
        `;
        toolContainer.innerHTML = html;
        sidebarLinks.forEach(a => a.classList.remove('active'));
        document.querySelector(`.sidebar-nav a[data-tool="${toolId}"]`)?.classList.add('active');
        if (toolId === 'system-monitor') startSystemMonitor();
      }

      function startSystemMonitor() {
        const statsEl = document.getElementById('systemStats');
        if (!statsEl) return;
        const update = () => {
          const usedRAM = (Math.random() * 8 + 4).toFixed(1);
          const cpu = Math.floor(Math.random() * 40 + 20);
          statsEl.innerHTML = currentLang === 'ar' ?
            `🖥️ الرام: ${usedRAM} GB / 16 GB | المعالج: ${cpu}%` :
            `🖥️ RAM: ${usedRAM} GB / 16 GB | CPU: ${cpu}%`;
        };
        update();
        setInterval(update, 3000);
      }

      function switchLanguage() {
        currentLang = currentLang === 'ar' ? 'en' : 'ar';
        langSwitch.textContent = currentLang === 'ar' ? 'English' : 'العربية';
        document.documentElement.lang = currentLang;
        document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
        document.body.style.fontFamily = currentLang === 'ar' ? 'var(--font-ar)' : 'var(--font-en)';
        // Update sidebar labels
        document.querySelectorAll('.sidebar-nav a span[data-lang]').forEach(span => {
          const key = span.getAttribute('data-lang');
          if (translations[currentLang][key]) {
            span.textContent = translations[currentLang][key];
          }
        });
        // Reload current tool
        const activeTool = document.querySelector('.sidebar-nav a.active');
        if (activeTool) {
          loadTool(activeTool.getAttribute('data-tool'));
        }
      }

      // ========== Event Listeners ==========
      sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          e.preventDefault();
          loadTool(this.getAttribute('data-tool'));
          if (window.innerWidth <= 768) sidebar.classList.remove('open');
        });
      });

      menuToggle.addEventListener('click', () => sidebar.classList.toggle('open'));
      langSwitch.addEventListener('click', switchLanguage);

      // ========== Initial Load ==========
      loadTool('dashboard');
    })();
  </script>
</body>
</html>
