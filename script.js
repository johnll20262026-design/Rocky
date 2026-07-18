const i18n = {
    zh: {
        'nav-home': '首页',
        'nav-about': '关于',
        'nav-gallery': '照片',
        'nav-skills': '特长',
        'nav-contact': '联系',
        'hero-tag': '武汉 · 中国',
        'hero-title-1': '你好，我是',
        'hero-subtitle': '财务人 · 吉他手 · 生活探索者',
        'hero-desc': '在数字与音符之间寻找平衡，用理性与感性诠释生活',
        'cta-explore': '了解更多',
        'scroll': '向下滚动',
        'about-title': '关于我',
        'about-intro': '一个在财务世界里严谨计算，在音乐世界里自由燃烧的人。白天与数字、报表打交道，夜晚抱起吉他，让旋律说话。',
        'info-location': '地区',
        'info-job': '职业',
        'info-job-value': '财务专业人士',
        'info-music': '音乐特长',
        'info-music-value': '电吉他 · 木吉他',
        'info-status': '状态',
        'info-status-value': '未婚',
        'about-quote': '音乐是我灵魂的语言，财务是我生活的根基。在理性与感性之间，我找到了属于自己的节奏。',
        'gallery-title': '照片墙',
        'gallery-subtitle': '记录生活中的每一个精彩瞬间',
        'photo1-caption': '山河之间，摇滚不止',
        'photo2-caption': '静谧时光，思考人生',
        'photo3-caption': '展翅高飞，自由翱翔',
        'skills-title': '我的特长',
        'skill-music-title': '音乐 · 吉他',
        'skill-music-desc': '精通电吉他与木吉他演奏，从摇滚到民谣，从布鲁斯到流行，用六根弦讲述故事。音乐是生命中不可或缺的部分，每一个音符都是情感的释放。',
        'skill-finance-title': '财务 · 专业',
        'skill-finance-desc': '财务专业背景，具备严谨的逻辑思维和数据分析能力。在数字的世界里保持清醒，用专业的态度处理每一个数据，确保每一份报表的精准。',
        'contact-title': '联系我',
        'contact-heading': '期待与你相识',
        'contact-desc': '无论是聊音乐、聊财务，还是分享生活，都欢迎添加我的微信。让我们一起创造更多可能！',
        'qr-hint': '微信二维码位置',
        'qr-desc': '请将你的微信二维码图片替换为 images/wechat-qr.png',
        'wechat-id': '微信号',
        'copy-id': '复制微信号',
        'copy-success': '微信号已复制！',
        'footer-text': '用音乐表达，用专业证明 © 2024 Rocky',
        'music-play': '点击播放音乐',
        'music-pause': '点击暂停音乐'
    },
    en: {
        'nav-home': 'Home',
        'nav-about': 'About',
        'nav-gallery': 'Photos',
        'nav-skills': 'Skills',
        'nav-contact': 'Contact',
        'hero-tag': 'Wuhan · China',
        'hero-title-1': "Hi, I'm",
        'hero-subtitle': 'Finance Professional · Guitarist · Life Explorer',
        'hero-desc': 'Finding balance between numbers and notes, interpreting life with reason and passion',
        'cta-explore': 'Learn More',
        'scroll': 'Scroll Down',
        'about-title': 'About Me',
        'about-intro': 'A person who calculates rigorously in the financial world and burns freely in the world of music. Working with numbers and reports during the day, picking up the guitar at night to let melodies speak.',
        'info-location': 'Location',
        'info-job': 'Profession',
        'info-job-value': 'Finance Professional',
        'info-music': 'Music',
        'info-music-value': 'Electric & Acoustic Guitar',
        'info-status': 'Status',
        'info-status-value': 'Single',
        'about-quote': 'Music is the language of my soul, finance is the foundation of my life. Between reason and passion, I found my own rhythm.',
        'gallery-title': 'Gallery',
        'gallery-subtitle': 'Capturing every wonderful moment in life',
        'photo1-caption': 'Between mountains and rivers, rock never stops',
        'photo2-caption': 'Quiet moments, reflecting on life',
        'photo3-caption': 'Spread wings and soar freely',
        'skills-title': 'My Skills',
        'skill-music-title': 'Music · Guitar',
        'skill-music-desc': 'Proficient in electric and acoustic guitar, from rock to folk, from blues to pop, telling stories through six strings. Music is an indispensable part of life, every note is an emotional release.',
        'skill-finance-title': 'Finance · Professional',
        'skill-finance-desc': 'Finance professional background with rigorous logical thinking and data analysis capabilities. Staying clear-headed in the world of numbers, handling every data with professional attitude, ensuring the precision of every report.',
        'contact-title': 'Contact Me',
        'contact-heading': 'Looking Forward to Meeting You',
        'contact-desc': "Whether it's about music, finance, or just sharing life, feel free to add me on WeChat. Let's create more possibilities together!",
        'qr-hint': 'WeChat QR Code',
        'qr-desc': 'Please replace with your WeChat QR image: images/wechat-qr.png',
        'wechat-id': 'WeChat ID',
        'copy-id': 'Copy WeChat ID',
        'copy-success': 'WeChat ID copied!',
        'footer-text': 'Expressed through music, proven through professionalism © 2024 Rocky',
        'music-play': 'Click to play music',
        'music-pause': 'Click to pause music'
    }
};

let currentLang = localStorage.getItem('lang') || 'zh';
let currentPhotoIndex = 2;
let isPlaying = false;
let autoPlayInterval = null;

document.addEventListener('DOMContentLoaded', function() {
    initLanguage();
    initNavigation();
    initPhotoGallery();
    initMusicPlayer();
    initScrollAnimations();
    initCopyButton();
    initNavScroll();
});

function initLanguage() {
    const langBtns = document.querySelectorAll('.lang-btn');
    
    setLanguage(currentLang);
    
    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;
            setLanguage(lang);
        });
    });
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('lang', lang);
    
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        if (i18n[lang][key]) {
            el.textContent = i18n[lang][key];
        }
    });
    
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
    
    updateMusicHint();
}

function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    document.querySelector('.logo').addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

function initNavScroll() {
    const navbar = document.querySelector('.navbar');
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
}

function initPhotoGallery() {
    const photoCards = document.querySelectorAll('.photo-card');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    function showPhoto(index) {
        currentPhotoIndex = index;
        
        photoCards.forEach((card, i) => {
            card.classList.remove('active');
            if (i === index) {
                card.classList.add('active');
            }
        });
        
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
    }
    
    function nextPhoto() {
        const next = (currentPhotoIndex + 1) % photoCards.length;
        showPhoto(next);
    }
    
    function prevPhoto() {
        const prev = (currentPhotoIndex - 1 + photoCards.length) % photoCards.length;
        showPhoto(prev);
    }
    
    showPhoto(2);
    
    nextBtn.addEventListener('click', nextPhoto);
    prevBtn.addEventListener('click', prevPhoto);
    
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => showPhoto(i));
    });
    
    photoCards.forEach((card, i) => {
        card.addEventListener('click', () => {
            if (i !== currentPhotoIndex) {
                showPhoto(i);
            }
        });
    });
    
    startAutoPlay();
    
    const photoStack = document.querySelector('.photo-stack');
    photoStack.addEventListener('mouseenter', stopAutoPlay);
    photoStack.addEventListener('mouseleave', startAutoPlay);
}

function startAutoPlay() {
    stopAutoPlay();
    autoPlayInterval = setInterval(() => {
        const photoCards = document.querySelectorAll('.photo-card');
        const next = (currentPhotoIndex + 1) % photoCards.length;
        showPhotoDirect(next);
    }, 4000);
}

function stopAutoPlay() {
    if (autoPlayInterval) {
        clearInterval(autoPlayInterval);
        autoPlayInterval = null;
    }
}

function showPhotoDirect(index) {
    const photoCards = document.querySelectorAll('.photo-card');
    const dots = document.querySelectorAll('.dot');
    
    currentPhotoIndex = index;
    
    photoCards.forEach((card, i) => {
        card.classList.remove('active');
        if (i === index) {
            card.classList.add('active');
        }
    });
    
    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
    });
}

function initMusicPlayer() {
    const musicToggle = document.getElementById('musicToggle');
    const bgMusic = document.getElementById('bgMusic');
    const musicPlayer = document.querySelector('.music-player');
    const musicHint = document.getElementById('musicHint');
    
    bgMusic.volume = 0.3;
    
    function toggleMusic() {
        if (isPlaying) {
            bgMusic.pause();
            musicPlayer.classList.remove('playing');
        } else {
            bgMusic.play().catch(() => {
                showToast(currentLang === 'zh' ? '请点击播放按钮开始音乐' : 'Click play to start music');
            });
            musicPlayer.classList.add('playing');
        }
        isPlaying = !isPlaying;
        updateMusicHint();
    }
    
    musicToggle.addEventListener('click', toggleMusic);
    
    document.addEventListener('click', function firstClick() {
        if (!isPlaying) {
            bgMusic.play().then(() => {
                isPlaying = true;
                musicPlayer.classList.add('playing');
                updateMusicHint();
            }).catch(() => {});
        }
        document.removeEventListener('click', firstClick);
    }, { once: true });
}

function updateMusicHint() {
    const musicHint = document.getElementById('musicHint');
    if (musicHint) {
        const key = isPlaying ? 'music-pause' : 'music-play';
        musicHint.querySelector('span').textContent = i18n[currentLang][key];
    }
}

function initScrollAnimations() {
    const sections = document.querySelectorAll('section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    sections.forEach(section => {
        observer.observe(section);
    });
    
    setTimeout(() => {
        document.querySelector('#home').classList.add('visible');
    }, 100);
}

function initCopyButton() {
    const copyBtn = document.getElementById('copyBtn');
    const wechatId = document.getElementById('wechatId');
    
    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(wechatId.textContent).then(() => {
            showToast(i18n[currentLang]['copy-success']);
        }).catch(() => {
            const textArea = document.createElement('textarea');
            textArea.value = wechatId.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            showToast(i18n[currentLang]['copy-success']);
        });
    });
}

function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2500);
}
