---
name: presentation
description: Convert any content (markdown, text, documents, research) into stunning single-file HTML presentations with full Arabic support, SVG icons, beautiful animations, and motion graphics. Use when creating slideshows, converting documents to presentations, or building visual content.
---

# Arabic HTML Presentation Generator

Convert any content into a beautiful, animated single-file HTML presentation with full Arabic language support and embedded English technical terms.

## When to Use This Skill

- Converting markdown files to presentations
- Creating Arabic slideshows from documents
- Building professional Arabic presentations
- Generating animated HTML presentations
- Creating visual summaries of business plans

## Core Requirements

When generating presentations, ALWAYS follow these specifications:

---

## Language & Direction (Arabic-First)

### Primary Language: Arabic (RTL)
- Set `lang="ar"` and `dir="rtl"` on the HTML element
- Write ALL content in Arabic
- Use Arabic for: titles, descriptions, labels, body text, navigation

### English Technical Terms
When English terms are needed (AI, API, ChatGPT, brand names), wrap them inline:
```html
<span class="en">AI</span>
<span class="en">ChatGPT</span>
<span class="en">API</span>
```

### CSS for Mixed Content
```css
/* Arabic text (default) */
body {
    font-family: 'Tajawal', sans-serif;
    direction: rtl;
    text-align: right;
}

/* English inline terms */
.en {
    font-family: 'Outfit', sans-serif;
    direction: ltr;
    display: inline-block;
    unicode-bidi: embed;
}
```

### Numbers
Use Western numerals (1, 2, 3) for all numbers and statistics.

---

## SVG Icon Library

Use these SVG icons throughout presentations. ALWAYS embed them inline (not as external files).

### Core Icons
```html
<!-- Vision Icon (Eye) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
    <circle cx="12" cy="12" r="3"/>
</svg>

<!-- Mission Icon (Target) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <circle cx="12" cy="12" r="6"/>
    <circle cx="12" cy="12" r="2"/>
</svg>

<!-- Problem Icon (X) -->
<svg class="icon icon-problem" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <line x1="15" y1="9" x2="9" y2="15"/>
    <line x1="9" y1="9" x2="15" y2="15"/>
</svg>

<!-- Solution Icon (Checkmark) -->
<svg class="icon icon-solution" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
    <polyline points="22 4 12 14.01 9 11.01"/>
</svg>

<!-- Arrow Right (for timeline) -->
<svg class="icon icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <line x1="5" y1="12" x2="19" y2="12"/>
    <polyline points="12 5 19 12 12 19"/>
</svg>

<!-- Users Icon -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
    <circle cx="9" cy="7" r="4"/>
    <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
    <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
</svg>

<!-- Money Icon -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <line x1="12" y1="1" x2="12" y2="23"/>
    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
</svg>

<!-- Chart Icon -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <line x1="18" y1="20" x2="18" y2="10"/>
    <line x1="12" y1="20" x2="12" y2="4"/>
    <line x1="6" y1="20" x2="6" y2="14"/>
</svg>

<!-- Graduation Cap -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
    <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
</svg>

<!-- Certificate -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <rect x="3" y="3" width="18" height="18" rx="2"/>
    <path d="M7 7h10M7 12h10M7 17h6"/>
</svg>

<!-- Strength Icon (Muscle) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/>
    <line x1="4" y1="22" x2="4" y2="15"/>
</svg>

<!-- Warning Icon (Weakness) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
    <line x1="12" y1="9" x2="12" y2="13"/>
    <line x1="12" y1="17" x2="12.01" y2="17"/>
</svg>

<!-- Rocket Icon (Opportunity) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
    <path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
</svg>

<!-- Shield Icon (Threat) -->
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
    <line x1="12" y1="8" x2="12" y2="12"/>
    <line x1="12" y1="16" x2="12.01" y2="16"/>
</svg>

<!-- Carousel Arrow Left -->
<svg class="carousel-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polyline points="15 18 9 12 15 6"/>
</svg>

<!-- Carousel Arrow Right -->
<svg class="carousel-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polyline points="9 18 15 12 9 6"/>
</svg>
```

### Icon Styling
```css
.icon {
    width: clamp(24px, 4vh, 40px);
    height: clamp(24px, 4vh, 40px);
    stroke: var(--accent-cyan);
}

.icon-problem {
    stroke: var(--accent-rose);
}

.icon-solution {
    stroke: var(--accent-emerald);
}

.icon-arrow {
    stroke: var(--accent-violet);
    width: clamp(32px, 5vh, 48px);
}
```

---

## Design Specifications

### Theme: Dark Professional
```css
:root {
    --bg-primary: #0a0e1a;
    --bg-secondary: #111827;
    --accent-cyan: #06b6d4;
    --accent-violet: #8b5cf6;
    --accent-amber: #f59e0b;
    --accent-rose: #f43f5e;
    --accent-emerald: #10b981;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
}
```

### Typography
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Tajawal:wght@300;400;500;700;800&display=swap');

body {
    font-family: 'Tajawal', sans-serif;
}

.en {
    font-family: 'Outfit', sans-serif;
}
```

---

## Scaling & Margins (CRITICAL)

```css
:root {
    --slide-padding-x: clamp(20px, 4vw, 60px);
    --slide-padding-y: clamp(15px, 2.5vh, 40px);
    --content-max-width: 1200px;
    --card-min-height: clamp(80px, 12vh, 150px);
    --card-padding: clamp(10px, 1.5vh, 20px);
    --grid-gap: clamp(8px, 1.2vh, 16px);
}

html {
    font-size: clamp(12px, 1.2vw, 16px);
    scroll-behavior: smooth;
    scroll-snap-type: y mandatory;
}

.slide {
    height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--slide-padding-y) var(--slide-padding-x);
    box-sizing: border-box;
    scroll-snap-align: start;
    position: relative;
    overflow: visible;
}

.slide-content {
    width: 100%;
    max-width: var(--content-max-width);
    max-height: calc(100vh - var(--slide-padding-y) * 2);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: clamp(8px, 1.5vh, 20px);
}

/* Height-based media queries */
@media (max-height: 700px) {
    :root {
        --card-min-height: 70px;
        --card-padding: 8px;
        --grid-gap: 6px;
    }
    html { font-size: clamp(11px, 1.1vw, 14px); }
}

@media (max-height: 550px) {
    :root {
        --card-min-height: 55px;
        --card-padding: 6px;
        --grid-gap: 5px;
    }
    html { font-size: clamp(10px, 1vw, 12px); }
}
```

---

## Timeline Layout (Problem/Solution)

Use horizontal timeline layout for problem/solution slides:

```html
<div class="timeline-container">
    <div class="timeline-row">
        <div class="timeline-card problem">
            <svg class="icon icon-problem"><!-- X icon --></svg>
            <span class="timeline-text">معظم كورسات <span class="en">AI</span> نظرية ومملة</span>
        </div>
        <svg class="icon icon-arrow"><!-- Arrow --></svg>
        <div class="timeline-card solution">
            <svg class="icon icon-solution"><!-- Check icon --></svg>
            <span class="timeline-text">تعليم عملي من مشاريع حقيقية</span>
        </div>
    </div>
    <!-- More rows... -->
</div>
```

```css
.timeline-container {
    display: flex;
    flex-direction: column;
    gap: var(--grid-gap);
    width: 100%;
    max-width: var(--content-max-width);
}

.timeline-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: clamp(10px, 2vw, 30px);
}

.timeline-card {
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border-radius: clamp(8px, 1.5vh, 16px);
    padding: var(--card-padding);
    display: flex;
    align-items: center;
    gap: clamp(8px, 1.5vh, 15px);
    min-width: clamp(200px, 35vw, 400px);
    max-width: 45%;
}

.timeline-card.problem {
    border: 2px solid var(--accent-rose);
}

.timeline-card.solution {
    border: 2px solid var(--accent-emerald);
}

.timeline-text {
    font-size: clamp(0.8rem, 1.6vh, 1.1rem);
    line-height: 1.4;
}

.icon-arrow {
    flex-shrink: 0;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.1); }
}
```

---

## Carousel Component (Products/Courses)

Use carousel for displaying courses or products:

```html
<div class="carousel-container">
    <button class="carousel-btn carousel-prev" aria-label="السابق">
        <svg class="carousel-arrow"><!-- Left arrow --></svg>
    </button>

    <div class="carousel-viewport">
        <div class="carousel-track">
            <div class="carousel-slide active">
                <!-- Course card 1 -->
            </div>
            <div class="carousel-slide">
                <!-- Course card 2 -->
            </div>
            <div class="carousel-slide">
                <!-- Course card 3 -->
            </div>
        </div>
    </div>

    <button class="carousel-btn carousel-next" aria-label="التالي">
        <svg class="carousel-arrow"><!-- Right arrow --></svg>
    </button>

    <div class="carousel-dots">
        <span class="carousel-dot active"></span>
        <span class="carousel-dot"></span>
        <span class="carousel-dot"></span>
    </div>
</div>
```

```css
.carousel-container {
    position: relative;
    width: 100%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: clamp(10px, 2vh, 20px);
}

.carousel-viewport {
    width: 100%;
    overflow: hidden;
    border-radius: clamp(12px, 2vh, 24px);
}

.carousel-track {
    display: flex;
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.carousel-slide {
    min-width: 100%;
    padding: clamp(15px, 3vh, 30px);
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: clamp(12px, 2vh, 24px);
    text-align: center;
}

.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 50%;
    width: clamp(36px, 5vh, 48px);
    height: clamp(36px, 5vh, 48px);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    z-index: 10;
}

.carousel-prev { right: calc(100% + 10px); }
.carousel-next { left: calc(100% + 10px); }

.carousel-btn:hover {
    background: var(--accent-violet);
    border-color: var(--accent-violet);
}

.carousel-dots {
    display: flex;
    gap: 8px;
}

.carousel-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--glass-border);
    cursor: pointer;
    transition: all 0.3s ease;
}

.carousel-dot.active {
    background: var(--accent-cyan);
    transform: scale(1.2);
}
```

```javascript
// Carousel functionality
function initCarousel(container) {
    const track = container.querySelector('.carousel-track');
    const slides = container.querySelectorAll('.carousel-slide');
    const dots = container.querySelectorAll('.carousel-dot');
    const prevBtn = container.querySelector('.carousel-prev');
    const nextBtn = container.querySelector('.carousel-next');
    let currentIndex = 0;

    function goToSlide(index) {
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;
        currentIndex = index;
        track.style.transform = `translateX(${index * 100}%)`;
        dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
        slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    }

    prevBtn?.addEventListener('click', () => goToSlide(currentIndex + 1)); // RTL: prev goes right
    nextBtn?.addEventListener('click', () => goToSlide(currentIndex - 1)); // RTL: next goes left
    dots.forEach((dot, i) => dot.addEventListener('click', () => goToSlide(i)));

    // Auto-advance every 5 seconds
    setInterval(() => goToSlide(currentIndex - 1), 5000);
}

document.querySelectorAll('.carousel-container').forEach(initCarousel);
```

---

## Navigation (Left Side for RTL)

```css
.nav-dots {
    position: fixed;
    left: clamp(10px, 2vw, 20px); /* LEFT side for RTL */
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: clamp(6px, 1vh, 10px);
    z-index: 100;
}

.nav-dot {
    width: clamp(8px, 1vh, 12px);
    height: clamp(8px, 1vh, 12px);
    border-radius: 50%;
    background: var(--glass-border);
    cursor: pointer;
    transition: all 0.3s ease;
}

.nav-dot.active {
    background: var(--accent-cyan);
    transform: scale(1.3);
}

.progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent-cyan), var(--accent-violet));
    z-index: 100;
    width: 0%;
    transition: width 0.1s ease;
}
```

---

## Full Keyboard Navigation

```javascript
document.addEventListener('keydown', (e) => {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = Array.from(slides).findIndex(slide => {
        const rect = slide.getBoundingClientRect();
        return rect.top >= -100 && rect.top <= 100;
    });
    if (currentSlide === -1) currentSlide = 0;

    switch(e.key) {
        case 'ArrowDown':
        case 'PageDown':
        case ' ':
            e.preventDefault();
            if (currentSlide < slides.length - 1) {
                slides[currentSlide + 1].scrollIntoView({ behavior: 'smooth' });
            }
            break;
        case 'ArrowUp':
        case 'PageUp':
            e.preventDefault();
            if (currentSlide > 0) {
                slides[currentSlide - 1].scrollIntoView({ behavior: 'smooth' });
            }
            break;
        case 'Home':
            e.preventDefault();
            slides[0].scrollIntoView({ behavior: 'smooth' });
            break;
        case 'End':
            e.preventDefault();
            slides[slides.length - 1].scrollIntoView({ behavior: 'smooth' });
            break;
        case 'f':
        case 'F':
            if (!e.ctrlKey && !e.metaKey) {
                e.preventDefault();
                if (document.fullscreenElement) {
                    document.exitFullscreen();
                } else {
                    document.documentElement.requestFullscreen();
                }
            }
            break;
        default:
            // Number keys 1-9 for direct slide access
            if (e.key >= '1' && e.key <= '9') {
                const slideIndex = parseInt(e.key) - 1;
                if (slideIndex < slides.length) {
                    e.preventDefault();
                    slides[slideIndex].scrollIntoView({ behavior: 'smooth' });
                }
            }
    }
});
```

---

## Auto-Split Content Guidelines

### Maximum Content Per Slide
- **Cards**: Maximum 6 cards (3x2 grid or 2 timeline rows)
- **Stats**: Maximum 5 stat items per row
- **Lists**: Maximum 6 items, then split to new slide
- **Tables**: Maximum 6 rows, then convert to cards or split

### When to Split
If content exceeds limits, create continuation slides:
```html
<!-- Slide: المميزات -->
<section class="slide">
    <h2>المميزات</h2>
    <!-- First 6 items -->
</section>

<!-- Slide: المميزات (تابع) -->
<section class="slide">
    <h2>المميزات <span class="continued">(تابع)</span></h2>
    <!-- Remaining items -->
</section>
```

```css
.continued {
    font-size: 0.7em;
    color: var(--text-secondary);
    font-weight: 400;
}
```

---

## Arabic Slide Templates

### 1. العنوان (Title Slide)
```html
<section class="slide" id="slide-title">
    <div class="bg-gradient"></div>
    <div class="floating-orb orb-1"></div>
    <div class="floating-orb orb-2"></div>
    <div class="slide-content">
        <div class="logo-container">
            <img src="{{IMAGE_logo}}" alt="الشعار">
        </div>
        <h1 class="main-title">اسم المشروع</h1>
        <p class="sub-title">العنوان الفرعي</p>
        <div class="stat-hero">
            <span class="stat-number-hero" data-target="600000">0</span>
            <span class="stat-label-hero">الرقم الرئيسي</span>
        </div>
        <p class="tagline">"الشعار أو الرسالة الرئيسية"</p>
    </div>
</section>
```

### 2. الرؤية والرسالة (Vision & Mission)
```html
<section class="slide" id="slide-vision">
    <div class="bg-gradient"></div>
    <div class="slide-content">
        <h2 class="section-title">الرؤية والرسالة</h2>
        <div class="cards-grid vision-mission">
            <div class="card">
                <svg class="icon"><!-- Vision icon --></svg>
                <div class="card-title">الرؤية</div>
                <div class="card-text">نص الرؤية هنا...</div>
            </div>
            <div class="card">
                <svg class="icon"><!-- Mission icon --></svg>
                <div class="card-title">الرسالة</div>
                <div class="card-text">نص الرسالة هنا...</div>
            </div>
        </div>
    </div>
</section>
```

### 3. المشكلة والحل (Problem & Solution)
```html
<section class="slide" id="slide-problem">
    <div class="bg-gradient"></div>
    <div class="slide-content">
        <h2 class="section-title">المشكلة والحل</h2>
        <div class="timeline-container">
            <div class="timeline-row">
                <div class="timeline-card problem">
                    <svg class="icon icon-problem"><!-- X --></svg>
                    <span class="timeline-text">وصف المشكلة</span>
                </div>
                <svg class="icon icon-arrow"><!-- Arrow --></svg>
                <div class="timeline-card solution">
                    <svg class="icon icon-solution"><!-- Check --></svg>
                    <span class="timeline-text">وصف الحل</span>
                </div>
            </div>
        </div>
    </div>
</section>
```

### 4. الأرقام الرئيسية (Key Metrics)
```html
<section class="slide" id="slide-metrics">
    <div class="bg-gradient"></div>
    <div class="slide-content">
        <h2 class="section-title">الأرقام الرئيسية</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <svg class="icon"><!-- Icon --></svg>
                <div class="stat-number" data-target="240">0</div>
                <div class="stat-label">الوصف</div>
            </div>
            <!-- More stats -->
        </div>
    </div>
</section>
```

### 5. المنتجات/الدورات (Products/Courses)
```html
<section class="slide" id="slide-products">
    <div class="bg-gradient"></div>
    <div class="slide-content">
        <h2 class="section-title">الدورات التدريبية</h2>
        <div class="carousel-container">
            <!-- Carousel implementation -->
        </div>
    </div>
</section>
```

### 6. تحليل SWOT
```html
<section class="slide" id="slide-swot">
    <div class="bg-gradient"></div>
    <div class="slide-content">
        <h2 class="section-title">تحليل <span class="en">SWOT</span></h2>
        <div class="swot-grid">
            <div class="swot-card strength">
                <div class="swot-title">
                    <svg class="icon"><!-- Strength --></svg>
                    نقاط القوة
                </div>
                <ul class="swot-list">
                    <li>نقطة 1</li>
                    <li>نقطة 2</li>
                </ul>
            </div>
            <!-- Weakness, Opportunity, Threat cards -->
        </div>
    </div>
</section>
```

### 7. الختام (Conclusion)
```html
<section class="slide" id="slide-conclusion">
    <div class="bg-gradient"></div>
    <div class="floating-orb orb-1"></div>
    <div class="floating-orb orb-2"></div>
    <div class="slide-content">
        <div class="logo-container">
            <img src="{{IMAGE_logo}}" alt="الشعار">
        </div>
        <h2 class="main-title">اسم المشروع</h2>
        <div class="quote-box">
            <div class="quote-text">"الرسالة الختامية"</div>
        </div>
        <div class="stats-grid final-stats">
            <!-- Key summary stats -->
        </div>
    </div>
</section>
```

---

## Background Effects

```css
.bg-gradient {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 30% 20%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 70% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
    pointer-events: none;
}

.floating-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.3;
    animation: float 15s ease-in-out infinite;
}

.orb-1 { width: 300px; height: 300px; background: var(--accent-violet); top: 10%; right: 5%; }
.orb-2 { width: 250px; height: 250px; background: var(--accent-cyan); bottom: 10%; left: 10%; animation-delay: -5s; }

@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-20px, 20px) scale(0.95); }
}
```

---

## Quote Box (Gradient Style)

```css
.quote-box {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(6, 182, 212, 0.2));
    border: 1px solid var(--glass-border);
    border-radius: clamp(12px, 2vh, 24px);
    padding: clamp(15px, 3vh, 35px) clamp(20px, 4vw, 50px);
    text-align: center;
    max-width: 800px;
    width: 100%;
}

.quote-text {
    font-size: clamp(1rem, 2.5vw, 1.6rem);
    font-weight: 600;
    line-height: 1.4;
}
```

---

## Animations

```css
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-20px, 20px) scale(0.95); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

.card, .stat-item, .timeline-card, .swot-card {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
}

.card.visible, .stat-item.visible, .timeline-card.visible, .swot-card.visible {
    opacity: 1;
    transform: translateY(0);
}
```

---

## Image Embedding System

### Logo Placement
- **Title slide**: Large centered logo
- **Conclusion slide**: Large centered logo
- **Other slides**: No logo (clean content)

### Placeholders
```html
<img src="{{IMAGE_logo}}" alt="الشعار" class="logo-image">
```

### Python Embedding Script
Generate `embed_images.py` with:
```python
IMAGES = {
    'logo': r'path/to/logo.png',
}
```

---

## File Naming Convention

Name files based on content title:
- Arabic title "أكاديمية لومينا" -> `Lumina_Academy_Presentation.html`
- English title "LUMINA AI" -> `LUMINA_AI_Presentation.html`

---

## Output Checklist

Every generated presentation must have:
- [ ] `lang="ar"` and `dir="rtl"` on HTML
- [ ] Full Arabic content (except technical terms)
- [ ] SVG icons (not emoji or text)
- [ ] Timeline layout for problem/solution
- [ ] Carousel for products/courses
- [ ] Navigation dots on LEFT
- [ ] Progress bar at top
- [ ] Full keyboard navigation
- [ ] Logo on title + conclusion only
- [ ] Floating orb backgrounds
- [ ] Animated counters for stats
- [ ] Responsive scaling with vh/vw units
- [ ] Height-based media queries
