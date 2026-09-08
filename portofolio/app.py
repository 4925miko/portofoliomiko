import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Portofolio |  Multimedia",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# DATA — EDIT THIS SECTION
# =========================
PROFILE = {
    "name": "Herlambang Sujatmiko",
    "role": "UI/UX, Designer Canva & Spesialis Multimedia",
    "location": "Yogyakarta, Indonesia",
    "email": "miko.gamping@email.com",
    "whatsapp": "https://wa.me/6285747808835",
    "instagram": "https://www.instagram.com/_mikoaja?stkn=bW81aGs5Zm14MzNo&utm_source=qr",
    "photo": "https://raw.githubusercontent.com/4925miko/portofolio/main/assets/profile.jpeg",
    "github": "https://github.com/4925miko",
    "cv_url": "https://canva.link/7n8331nv7f65hpc",
}

# =========================
# PROJECT IMAGES
# =========================
BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = BASE_DIR / "assets" / "projects"


def project_image_src(filename, title):
    """Baca gambar project langsung dari folder assets/projects."""
    if not filename:
        return f"https://placehold.co/1200x720/17171c/f4f4f5?text={title.replace(' ', '+')}"

    # Tetap mendukung URL gambar kalau suatu saat diperlukan.
    if filename.startswith(("http://", "https://", "data:")):
        return filename

    image_path = PROJECTS_DIR / filename

    if image_path.exists():
        suffix = image_path.suffix.lower()
        mime = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
            ".gif": "image/gif",
        }.get(suffix, "application/octet-stream")

        encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        return f"data:{mime};base64,{encoded}"

    # Kalau file belum dimasukkan, kartu tetap tampil dengan placeholder.
    return f"https://placehold.co/1200x720/17171c/f4f4f5?text=Upload+{title.replace(' ', '+')}"

ABOUT = """
Saya merupakan Fresh Graduate S1 Informatika, Universitas AMIKOM Yogyakarta,
dengan penjurusan Multimedia dan fokus pada bidang UI/UX, Design Canva serta Multimedia.
Memiliki kemampuan dalam merancang antarmuka yang kreatif, fungsional, dan
berorientasi pada pengalaman pengguna, serta mengoperasikan berbagai software
pendukung pekerjaan di bidang desain dan multimedia.

Saya mampu bekerja secara individu maupun dalam tim, memiliki kemampuan
komunikasi yang baik dalam Bahasa Indonesia dan Bahasa Inggris, serta memiliki
semangat untuk terus belajar dan mengembangkan keterampilan di bidang teknologi kreatif.
"""

SKILLS = [
    "UI/UX Design", "Figma", "Communication Skills", "Prototyping","Analisis Data","Data Entry",
    "Customer Service", "HTML", "CSS", "JavaScript","Processing","Problem Solving","Game 2D","General Office Work",
    "Canva", "Foto&Video Editing", "Multimedia Design", "Streamlit","Media Interaktif","Leadership","Desain Grafis"
]

# Gambar project cukup diletakkan di: assets/projects/
# Contoh:
# assets/projects/game-pancasila.jpg
# assets/projects/dwikarya.png
# assets/projects/ui-mobile.jpg

PROJECTS = [
    {
        "title": "Game Edukasi Pancasila",
        "category": "UI/UX • Game • Multimedia",
        "year": "2026",
        "description": (
            "Media pembelajaran interaktif 2D berbasis desktop dalam bentuk game edukasi "
            "untuk membantu siswa kelas 2 memahami nilai-nilai Pancasila."
        ),
        "tools": ["Processing", "UI/UX", "Multimedia", "MDLC"],
        "image": "https://raw.githubusercontent.com/4925miko/portofolio/main/assets/projects/gamepancasila.png",
        "demo": "https://drive.google.com/drive/folders/1AvFV6_gHyihYT-XQ6ZurVYKOaMDdKQmz?usp=sharing",
        
    },
    {
        "title": "Landing Page Dwikarya",
        "category": "Front-End • Desain Web",
        "year": "2024",
        "description": (
            "Landing page responsif dengan fokus pada struktur informasi yang jelas, "
            "visual modern, dan pengalaman pengguna yang sederhana."
        ),
        "tools": ["HTML", "CSS", "JavaScript"],
        "image": "https://raw.githubusercontent.com/4925miko/portofolio/main/assets/projects/dwikarya.png",
        "demo": "https://dwikarya-umkm.streamlit.app/",
        
    },
    {
        "title": "Konsep UI Aplikasi Mobile",
        "category": "UI/UX • Prototipe",
        "year": "2026",
        "description": (
            "Konsep antarmuka aplikasi mobile dengan pendekatan desain berorientasi pengguna, "
            "mulai dari wireframe hingga prototipe high-fidelity."
        ),
        "tools": ["Figma", "Wireframe", "Prototype"],
        "image": "ui-mobile.jpg",
        "demo": "#",
        
    },
]

# =========================
# STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root{
    --bg:#0b0b0f;
    --card:#121218;
    --soft:#191922;
    --text:#f5f5f7;
    --muted:#a1a1aa;
    --line:#27272f;
    --accent:#a78bfa;
    --accent2:#67e8f9;
}

html, body, [class*="css"]  {
    font-family:'DM Sans', sans-serif;
}

.stApp{
    background:
      radial-gradient(circle at 15% 0%, rgba(167,139,250,.12), transparent 28%),
      radial-gradient(circle at 85% 10%, rgba(103,232,249,.08), transparent 25%),
      var(--bg);
    color:var(--text);
}

.block-container{
    max-width:1180px;
    padding-top:1.4rem;
    padding-bottom:4rem;
}

header[data-testid="stHeader"]{
    background:transparent;
}

#MainMenu, footer {visibility:hidden;}

.nav{
    position:sticky;
    top:.8rem;
    z-index:20;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:.8rem 1rem;
    margin-bottom:4.4rem;
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    background:rgba(14,14,19,.78);
    backdrop-filter:blur(18px);
    box-shadow:0 10px 40px rgba(0,0,0,.18);
}

.brand{
    font-weight:700;
    letter-spacing:.04em;
    font-size:.95rem;
}

.navlinks{
    color:var(--muted);
    font-size:.88rem;
}

.hero-kicker{
    display:inline-flex;
    align-items:center;
    gap:.5rem;
    color:#d8d8de;
    font-size:.86rem;
    border:1px solid var(--line);
    background:rgba(255,255,255,.025);
    padding:.45rem .75rem;
    border-radius:999px;
    margin-bottom:1.25rem;
}

.dot{
    width:7px;height:7px;border-radius:50%;
    background:#6ee7b7;
    box-shadow:0 0 14px rgba(110,231,183,.8);
}

.hero-title{
    font-family:'Playfair Display', serif;
    font-size:clamp(3.2rem, 7.5vw, 6.8rem);
    line-height:.96;
    margin:0;
    letter-spacing:-.045em;
}

.gradient{
    background:linear-gradient(90deg, #f5f5f7 0%, #a78bfa 46%, #67e8f9 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-desc{
    max-width:750px;
    font-size:1.08rem;
    line-height:1.75;
    color:var(--muted);
    margin-top:1.6rem;
}

.btnrow{
    display:flex;
    gap:.75rem;
    flex-wrap:wrap;
    margin-top:1.7rem;
}

.btn{
    display:inline-block;
    text-decoration:none!important;
    border-radius:12px;
    padding:.76rem 1.05rem;
    font-weight:600;
    font-size:.9rem;
    border:1px solid var(--line);
    transition:.2s ease;
}

.btn-primary{
    background:#f4f4f5;
    color:#111116!important;
}

.btn-secondary{
    background:transparent;
    color:#f4f4f5!important;
}

.btn:hover{
    transform:translateY(-2px);
    border-color:#52525b;
}

.section{
    margin-top:8rem;
}

.eyebrow{
    color:#a78bfa;
    text-transform:uppercase;
    letter-spacing:.16em;
    font-weight:700;
    font-size:.72rem;
    margin-bottom:.75rem;
}

.section-title{
    font-family:'Playfair Display', serif;
    font-size:clamp(2.2rem,4vw,3.4rem);
    margin:0 0 1rem 0;
    letter-spacing:-.025em;
}

.section-copy{
    color:var(--muted);
    line-height:1.8;
    max-width:820px;
}

.stat{
    padding:1.2rem;
    border:1px solid var(--line);
    border-radius:16px;
    background:linear-gradient(180deg, rgba(255,255,255,.025), rgba(255,255,255,.01));
    min-height:118px;
}

.stat-num{
    font-family:'Playfair Display',serif;
    font-size:2rem;
    margin-bottom:.2rem;
}

.stat-label{
    color:var(--muted);
    font-size:.83rem;
}

.skillwrap{
    display:flex;
    flex-wrap:wrap;
    gap:.55rem;
    margin-top:1.3rem;
}

.skill{
    border:1px solid var(--line);
    background:rgba(255,255,255,.02);
    border-radius:999px;
    padding:.55rem .8rem;
    font-size:.84rem;
    color:#d4d4d8;
}

.project{
    border:1px solid var(--line);
    border-radius:22px;
    background:linear-gradient(180deg, rgba(255,255,255,.032), rgba(255,255,255,.012));
    overflow:hidden;
    margin-bottom:1.25rem;
    transition:.25s ease;
}

.project:hover{
    transform:translateY(-3px);
    border-color:#3f3f46;
}

.project img{
    width:100%;
    aspect-ratio:16/9;
    object-fit:cover;
    display:block;
    border-bottom:1px solid var(--line);
}

.project-body{
    padding:1.25rem;
}

.project-meta{
    display:flex;
    justify-content:space-between;
    gap:1rem;
    color:#a1a1aa;
    font-size:.78rem;
    margin-bottom:.65rem;
}

.project-title{
    font-size:1.28rem;
    font-weight:700;
    margin-bottom:.55rem;
}

.project-desc{
    color:var(--muted);
    font-size:.9rem;
    line-height:1.65;
    min-height:76px;
}

.tags{
    display:flex;
    flex-wrap:wrap;
    gap:.38rem;
    margin:.9rem 0 1.1rem;
}

.tag{
    padding:.35rem .55rem;
    border-radius:8px;
    background:#1b1b24;
    color:#c4b5fd;
    font-size:.72rem;
}

.mini-links{
    display:flex;
    gap:.7rem;
}

.mini-links a{
    color:#e4e4e7!important;
    font-size:.82rem;
    text-decoration:none!important;
    border-bottom:1px solid #52525b;
    padding-bottom:2px;
}

.contact-box{
    padding:2rem;
    border:1px solid var(--line);
    border-radius:24px;
    background:
      radial-gradient(circle at 90% 20%, rgba(103,232,249,.1), transparent 30%),
      radial-gradient(circle at 10% 90%, rgba(167,139,250,.11), transparent 34%),
      #101016;
}

.contact-title{
    font-family:'Playfair Display',serif;
    font-size:clamp(2.4rem,5vw,4.2rem);
    line-height:1;
    margin-bottom:1rem;
}

.contact-copy{
    color:var(--muted);
    max-width:650px;
    line-height:1.7;
}

.footerline{
    border-top:1px solid var(--line);
    margin-top:5rem;
    padding-top:1.25rem;
    color:#71717a;
    font-size:.78rem;
    display:flex;
    justify-content:space-between;
    flex-wrap:wrap;
    gap:.6rem;
}

@media (max-width:700px){
    .block-container{padding-left:1rem;padding-right:1rem;}
    .navlinks{display:none;}
    .section{margin-top:5.5rem;}
    .hero-title{font-size:3.45rem;}
    .project-desc{min-height:auto;}
}

.profile-photo-wrap{
    position:absolute;
    right:0;
    top:0;
    width:220px;
    z-index:2;
    transform:translateY(-8px);
}
.profile-photo{
    width:100%;
    aspect-ratio:1/1;
    object-fit:cover;
    border-radius:24px;
    border:1px solid rgba(255,255,255,.12);
    box-shadow:0 20px 55px rgba(0,0,0,.32);
    background:#15151c;
}
.profile-photo-fallback{
    width:100%;
    aspect-ratio:1/1;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:24px;
    border:1px solid rgba(255,255,255,.12);
    background:
      radial-gradient(circle at 30% 20%, rgba(167,139,250,.2), transparent 34%),
      #15151c;
    color:#f5f5f7;
    font-family:'Playfair Display',serif;
    font-size:3rem;
    box-shadow:0 20px 55px rgba(0,0,0,.32);
}
.social-buttons{
    display:flex;
    gap:.55rem;
    flex-wrap:wrap;
    margin-top:1rem;
}
.social-btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:.48rem .72rem;
    border:1px solid var(--line);
    border-radius:999px;
    background:rgba(255,255,255,.02);
    color:#e4e4e7!important;
    text-decoration:none!important;
    font-size:.78rem;
    transition:.2s ease;
}
.social-btn:hover{
    transform:translateY(-2px);
    border-color:#52525b;
}
@media (max-width:900px){
    .profile-photo-wrap{display:none;}
}

</style>
""", unsafe_allow_html=True)

# =========================
# NAV
# =========================
st.markdown(f"""
<div class="nav">
    <div class="brand">✦ {PROFILE['name'].upper()}</div>
    <div class="navlinks">UI/UX &nbsp;&nbsp;•&nbsp;&nbsp; MULTIMEDIA &nbsp;&nbsp;•&nbsp;&nbsp; FRONT-END</div>
</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

_photo_html = (
    f'<img class="profile-photo" '
    f'src="{PROFILE["photo"]}" '
    f'alt="Foto profil {PROFILE["name"]}">'
)

else:
    _photo_html = '<div class="profile-photo-fallback">HS</div>'

_social_html = (
    f'<div class="social-buttons">'
    f'<a class="social-btn" href="{PROFILE["whatsapp"]}" target="_blank">WhatsApp</a>'
    f'<a class="social-btn" href="{PROFILE["instagram"]}" target="_blank">Instagram</a>'
    f'</div>'
)

st.markdown(f"""
<div id="home">
    <div class="hero-kicker"><span class="dot"></span> Open to work & collaboration</div>
    <h1 class="hero-title">
        Merancang pengalaman<br>
        digital yang <span class="gradient">bermakna.</span>
    </h1>
    <div class="hero-desc">
        Halo, saya <b style="color:#f5f5f7">{PROFILE['name']}</b> — {PROFILE['role']}.
        Fresh Graduate S1 Informatika Universitas AMIKOM Yogyakarta dengan penjurusan Multimedia,
        berfokus pada pengalaman pengguna, visual yang kuat, dan solusi digital yang fungsional.
    </div>
    <div class="btnrow">
        <a class="btn btn-primary" href="#projects">Lihat karya pilihan ↗</a>
        <a class="btn btn-secondary"
   href="https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}&su=Konsultasi%20Proyek%20Portofolio"
   target="_blank">
    Mari berdiskusi
</a>
    {_social_html}
    <div class="profile-photo-wrap">{_photo_html}</div>
</div>
""", unsafe_allow_html=True)
# =========================
# ABOUT
# =========================
st.markdown('<div class="section" id="about">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">01 / Tentang Saya</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Kreatif dalam ide,<br>kuat dalam teknologi.</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-copy">{ABOUT}</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="stat"><div class="stat-num">S1</div><div class="stat-label">Informatika • Universitas AMIKOM Yogyakarta</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat"><div class="stat-num">UI/UX</div><div class="stat-label">Desain figma berorientasi pengguna & prototipe</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat"><div class="stat-num">Multimedia</div><div class="stat-label">Desain Canva • Multimedia • Front-End • Editor Foto&Video </div></div>', unsafe_allow_html=True)

st.markdown('<div class="skillwrap">' + ''.join([f'<span class="skill">{s}</span>' for s in SKILLS]) + '</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PROJECTS
# =========================
st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">02 / Proyek Pilihan</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Proyek yang mengubah ide<br>menjadi pengalaman.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">Beberapa proyek pilihan. Struktur ini dibuat agar mudah dikembangkan—'
    ' <b>PROJECTS</b> pada file app.py.</div>',
    unsafe_allow_html=True
)

for i in range(0, len(PROJECTS), 2):
    cols = st.columns(2)
    for j in range(2):
        idx = i + j
        if idx >= len(PROJECTS):
            break
        p = PROJECTS[idx]
        with cols[j]:
            tags = ''.join([f'<span class="tag">{t}</span>' for t in p["tools"]])
            image_src = project_image_src(p["image"], p["title"])
            st.markdown(f"""
            <div class="project">
                <img src="{image_src}" alt="{p['title']}">
                <div class="project-body">
                    <div class="project-meta">
                        <span>{p['category']}</span>
                        <span>{p['year']}</span>
                    </div>
                    <div class="project-title">{p['title']}</div>
                    <div class="project-desc">{p['description']}</div>
                    <div class="tags">{tags}</div>
                    <div class="mini-links">
                        <a href="{p['demo']}" target="_blank">TO Projects & Demo ↗</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# SERVICES / VALUE
# =========================
st.markdown('<div class="section" id="expertise">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">03 / Keahlian</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Dari konsep hingga<br>eksekusi visual.</div>', unsafe_allow_html=True)

e1, e2, e3 = st.columns(3)
cards = [
    ("01", "UI/UX Design", "Alur pengguna, desain antarmuka, prototipe, dan evaluasi pengalaman pengguna."),
    ("02", "Multimedia", "Konten visual, media interaktif&Game 2D, Desain Canva, Penyuntingan video, Dan Kebutuhan desain digital lainnya."),
    ("03", "Front-End", "Implementasi antarmuka web menggunakan HTML, CSS, JavaScript, serta prototipe menggunakan Streamlit."),
]
for col, (num, title, text) in zip([e1, e2, e3], cards):
    with col:
        st.markdown(
            f'<div class="stat" style="min-height:180px">'
            f'<div style="color:#71717a;font-size:.75rem;margin-bottom:1rem">{num}</div>'
            f'<div style="font-size:1.1rem;font-weight:700;margin-bottom:.5rem">{title}</div>'
            f'<div style="color:#a1a1aa;font-size:.86rem;line-height:1.65">{text}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
st.markdown(f"""
<div class="contact-box">
    <div class="eyebrow">04 / Kontak</div>
    <div class="contact-title">Punya proyek?<br><span class="gradient">Mari kita wujudkan.</span></div>
    <div class="contact-copy">
        Terbuka untuk kesempatan kerja, magang, freelance, dan kolaborasi di bidang
        UI/UX Design, Multimedia, maupun Desain Canva.
    </div>
    <div class="btnrow">
        <a class="btn btn-secondary"
   href="https://mail.google.com/mail/?view=cm&fs=1&to={PROFILE['email']}&su=Konsultasi%20Proyek%20Portofolio"
   target="_blank">
    Mari berdiskusi
</a>
        <a class="btn btn-secondary" href="{PROFILE['github']}" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="footerline">
    <span>© 2026 {PROFILE['name']}. Hak cipta dilindungi.</span>
    <span>{PROFILE['location']} • Dibuat dengan Streamlit</span>
</div>
""", unsafe_allow_html=True)
