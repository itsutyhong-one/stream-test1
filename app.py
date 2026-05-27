import streamlit as st

st.set_page_config(
    page_title="홍혜림 | Portfolio",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nunito:ital,wght@0,400;0,600;0,700;0,900;1,700&family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Nunito', 'Noto Sans KR', sans-serif;
}

h1, h2, h3, .sec-title, .hero-name, .proj-name, .tl-title, .cta-title, .stamp {
    font-family: 'Jua', 'Noto Sans KR', sans-serif !important;
}

.block-container {
    padding: 0 2rem 4rem !important;
    max-width: 1080px !important;
}

/* 전체 배경 — 연그레이 + 은은한 빨간 도트 */
section[data-testid="stAppViewContainer"] {
    background-color: #eeeceb;
    background-image: radial-gradient(circle, rgba(210,60,60,0.35) 1.2px, transparent 1.2px);
    background-size: 20px 20px;
}

/* ─── 히어로 카드 ─── */
.dot-band {
    background: #fff;
    border: 2.5px solid #3d3d3d;
    border-radius: 20px;
    padding: 2.8rem 2.5rem 2.4rem;
    margin-bottom: 2rem;
    box-shadow: 6px 6px 0 #3d3d3d;
}

/* 이름 */
.hero-name {
    font-family: 'Jua', 'Noto Sans KR', sans-serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 900;
    color: #3d3d3d;
    line-height: 1.0;
    letter-spacing: -0.03em;
    margin-bottom: 0.6rem;
}
.hero-name em {
    font-style: italic;
    color: #e63030;
}
.hero-role-tag {
    display: inline-block;
    background: #e63030;
    color: #fff;
    font-weight: 900;
    font-size: 0.82rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 5px 16px;
    border-radius: 100px;
    margin-bottom: 1rem;
}
.hero-desc {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.8;
    max-width: 500px;
    font-weight: 400;
}

/* 아바타 */
.avatar-circle {
    width: 130px; height: 130px;
    border-radius: 50%;
    border: 5px solid #fff;
    background: #ffcfcf;
    display: flex; align-items: center; justify-content: center;
    font-size: 3.2rem;
    line-height: 1;
    box-shadow: 6px 6px 0 rgba(0,0,0,0.15);
    margin: 0 auto;
}

/* ─── 스탬프 뱃지 ─── */
.stamp-row {
    display: flex; gap: 0.8rem; flex-wrap: wrap;
    margin-bottom: 2rem;
}
.stamp {
    background: #fff;
    border: 2.5px solid #3d3d3d;
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    font-size: 0.82rem;
    font-weight: 700;
    color: #3d3d3d;
    box-shadow: 3px 3px 0 #3d3d3d;
    display: inline-flex; align-items: center; gap: 6px;
}
.stamp.red {
    background: #e63030;
    color: #fff;
    border-color: #b82020;
    box-shadow: 3px 3px 0 #b82020;
}

/* ─── 섹션 카드 ─── */
.sec-card {
    background: #fff;
    border: 2px solid #3d3d3d;
    border-radius: 18px;
    padding: 1.8rem 2rem;
    box-shadow: 5px 5px 0 #3d3d3d;
    margin-bottom: 1.2rem;
}
.sec-card.red-card {
    background: #e63030;
    border-color: #b82020;
    box-shadow: 5px 5px 0 #b82020;
}
.sec-card.dot-card {
    background-image: radial-gradient(circle, #ddd 1.2px, transparent 1.2px);
    background-size: 14px 14px;
    background-color: #f8f6f3;
}

/* ─── 섹션 라벨 ─── */
.sec-label {
    font-size: 0.68rem;
    font-weight: 900;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #e63030;
    margin-bottom: 0.3rem;
}
.sec-title {
    font-size: 1.35rem;
    font-weight: 900;
    color: #3d3d3d;
    letter-spacing: -0.02em;
    margin-bottom: 1.4rem;
    line-height: 1.2;
}
.sec-title-white {
    font-size: 1.35rem;
    font-weight: 900;
    color: #fff;
    letter-spacing: -0.02em;
    margin-bottom: 1.4rem;
}

/* ─── 스킬 바 ─── */
.skill-row { margin-bottom: 0.9rem; }
.skill-top {
    display: flex; justify-content: space-between;
    font-size: 0.84rem; font-weight: 700; color: #3d3d3d;
    margin-bottom: 5px;
}
.skill-pct { color: #888; font-weight: 500; }
.skill-track {
    height: 10px;
    background: #ece9e5;
    border-radius: 100px;
    overflow: hidden;
    border: 1.5px solid #d0ccc7;
}
.skill-fill {
    height: 100%;
    background: #3d3d3d;
    border-radius: 100px;
}
.skill-fill.red { background: #e63030; }
.skill-fill.gray { background: #888; }

/* ─── 타임라인 ─── */
.tl-item {
    display: flex; gap: 1rem;
    margin-bottom: 1.4rem;
    position: relative;
}
.tl-item:not(:last-child)::before {
    content: '';
    position: absolute;
    left: 5px; top: 14px;
    width: 1.5px;
    height: calc(100% + 4px);
    background: repeating-linear-gradient(to bottom, #ccc 0px, #ccc 4px, transparent 4px, transparent 8px);
}
.tl-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: #e63030;
    border: 2px solid #3d3d3d;
    flex-shrink: 0;
    margin-top: 5px;
}
.tl-dot.gray { background: #888; }
.tl-period {
    font-size: 0.72rem; font-weight: 800;
    color: #e63030;
    letter-spacing: 0.05em;
    display: block; margin-bottom: 3px;
    text-transform: uppercase;
}
.tl-period.gray { color: #888; }
.tl-title { font-size: 0.95rem; font-weight: 800; color: #3d3d3d; margin-bottom: 2px; }
.tl-role { font-size: 0.82rem; color: #e63030; font-weight: 700; margin-bottom: 2px; }
.tl-sub { font-size: 0.81rem; color: #666; line-height: 1.6; }

/* ─── 프로젝트 카드 ─── */
.proj-card {
    background: #fff;
    border: 2px solid #3d3d3d;
    border-radius: 16px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 4px 4px 0 #3d3d3d;
    transition: transform 0.15s, box-shadow 0.15s;
}
.proj-card:hover {
    transform: translate(-2px, -2px);
    box-shadow: 6px 6px 0 #3d3d3d;
}
.proj-icon { font-size: 1.7rem; margin-bottom: 0.5rem; }
.proj-name { font-size: 0.95rem; font-weight: 800; color: #3d3d3d; margin-bottom: 5px; }
.proj-desc { font-size: 0.82rem; color: #666; line-height: 1.7; margin-bottom: 10px; }
.proj-tag {
    display: inline-block;
    font-size: 0.72rem; font-weight: 700;
    padding: 2px 9px;
    border-radius: 100px;
    margin: 2px 2px 0 0;
    border: 1.5px solid #3d3d3d;
    color: #3d3d3d;
    background: transparent;
}
.proj-tag.red-tag {
    background: #e63030;
    color: #fff;
    border-color: #e63030;
}

/* ─── 자격증 ─── */
.cert-row {
    display: flex; align-items: center; gap: 10px;
    padding: 0.65rem 0;
    border-bottom: 1.5px dashed #d0ccc7;
}
.cert-icon {
    width: 34px; height: 34px;
    background: #ece9e5;
    border: 2px solid #3d3d3d;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem; flex-shrink: 0;
}
.cert-name { font-size: 0.87rem; font-weight: 700; color: #3d3d3d; }
.cert-meta { font-size: 0.74rem; color: #888; }

/* ─── 관심분야 ─── */
.int-chip {
    display: block;
    background: #fff;
    border: 2px solid #3d3d3d;
    border-radius: 10px;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.5rem;
    font-size: 0.84rem;
    font-weight: 700;
    color: #3d3d3d;
    box-shadow: 2px 2px 0 #3d3d3d;
}

/* ─── 연락처 CTA ─── */
.cta-wrap {
    background-color: #3d3d3d;
    background-image: radial-gradient(circle, rgba(230,48,48,0.35) 1.5px, transparent 1.5px);
    background-size: 20px 20px;
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 2rem;
    border: 2px solid #3d3d3d;
    box-shadow: 6px 6px 0 #e63030;
}
.cta-title {
    font-size: 2rem; font-weight: 900;
    color: #fff; letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
}
.cta-title em { color: #ff7070; font-style: italic; }
.cta-sub { font-size: 0.9rem; color: #aaa; margin-bottom: 1.6rem; }
.cta-email {
    display: inline-block;
    background: #e63030;
    color: #fff;
    font-weight: 800; font-size: 0.95rem;
    padding: 12px 32px;
    border-radius: 100px;
    border: 2px solid #fff;
    box-shadow: 4px 4px 0 #fff;
    letter-spacing: 0.02em;
}

.footer-note {
    text-align: center;
    color: #bbb;
    font-size: 0.76rem;
    margin-top: 1.8rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* 구분선 */
.divider {
    height: 2px;
    background: repeating-linear-gradient(to right, #3d3d3d 0px, #3d3d3d 8px, transparent 8px, transparent 14px);
    margin: 2rem 0;
    opacity: 0.12;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  히어로 — 빨간 도트 밴드
# ══════════════════════════════════════════════
h_left, h_right = st.columns([3, 1], gap="medium")

with h_left:
    st.markdown("""
    <div class="dot-band">
        <div class="hero-role-tag">● Data Engineer &amp; Developer</div>
        <h1 class="hero-name">Hong <em>Hye Lim</em></h1>
        <p class="hero-desc">
            데이터와 코드로 문제를 해결합니다.<br>
            에너지 IT 분야의 디지털 전환을 이끌고<br>
            사용자 중심의 서비스를 만듭니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with h_right:
    st.markdown("""
    <div style="padding-top:1.5rem;text-align:center;">
        <div class="avatar-circle">👩‍💻</div>
        <div style="margin-top:1rem;font-size:0.78rem;font-weight:700;color:#888;
                    letter-spacing:0.1em;text-transform:uppercase;">
            한전KDN<br>
            <span style="color:#e63030;">● 나주, Korea</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 스탬프 뱃지 행
st.markdown("""
<div class="stamp-row">
    <span class="stamp red">⚡ Energy IT</span>
    <span class="stamp">🐍 Python</span>
    <span class="stamp">📊 Data Engineering</span>
    <span class="stamp">🌐 Web Dev</span>
    <span class="stamp">☁️ Cloud</span>
    <span class="stamp">📧 honghyelim.22@kdn.com</span>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  본문 2단
# ══════════════════════════════════════════════
left, right = st.columns(2, gap="large")

# ── 왼쪽: 스킬 + 자격증
with left:
    st.markdown("""
    <div class="sec-card">
        <div class="sec-label">SKILLS</div>
        <div class="sec-title">기술 스택</div>
    """, unsafe_allow_html=True)

    skills = [
        ("Python",                  93, "red"),
        ("SQL / PostgreSQL",        86, ""),
        ("Streamlit",               90, "red"),
        ("JavaScript / HTML / CSS", 79, "gray"),
        ("Pandas · NumPy",          88, ""),
        ("Git / GitHub",            84, "gray"),
        ("Docker / Linux",          71, "gray"),
        ("AWS · Supabase",          74, ""),
    ]
    for name, pct, cls in skills:
        st.markdown(f"""
        <div class="skill-row">
            <div class="skill-top"><span>{name}</span><span class="skill-pct">{pct}%</span></div>
            <div class="skill-track">
                <div class="skill-fill {cls}" style="width:{pct}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-card dot-card">
        <div class="sec-label">CERTIFICATIONS</div>
        <div class="sec-title">자격증 &amp; 수료</div>
    """, unsafe_allow_html=True)

    certs = [
        ("🏅", "정보처리기사",           "한국산업인력공단",     "2023"),
        ("📊", "ADsP 데이터분석준전문가",  "한국데이터산업진흥원",  "2022"),
        ("🗄️", "SQLD SQL개발자",         "한국데이터산업진흥원",  "2022"),
        ("☁️", "AWS 클라우드 컴퓨팅 수료", "Amazon Web Services", "2024"),
    ]
    for icon, name, issuer, year in certs:
        st.markdown(f"""
        <div class="cert-row">
            <div class="cert-icon">{icon}</div>
            <div>
                <div class="cert-name">{name}</div>
                <div class="cert-meta">{issuer} · {year}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ── 오른쪽: 경력 + 학력 + 관심
with right:
    st.markdown("""
    <div class="sec-card">
        <div class="sec-label">EXPERIENCE</div>
        <div class="sec-title">경력 사항</div>
    """, unsafe_allow_html=True)

    career = [
        ("2022.07 — 현재",    "",     "한전KDN",
         "Data Engineer · IT전략팀",
         "전력 설비 운영 데이터 분석 시스템 개발, 사내 DX 과제 수행, DR 스케줄링 PoC"),
        ("2021.01 — 2022.06", "gray", "스타트업 A사",
         "풀스택 개발자 (인턴 → 정직원)",
         "사용자 대시보드 및 REST API 개발, Python 백엔드 설계"),
    ]
    for period, dot_cls, company, role, desc in career:
        st.markdown(f"""
        <div class="tl-item">
            <div class="tl-dot {dot_cls}"></div>
            <div>
                <span class="tl-period {dot_cls}">{period}</span>
                <div class="tl-title">{company}</div>
                <div class="tl-role">{role}</div>
                <div class="tl-sub">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-card">
        <div class="sec-label">EDUCATION</div>
        <div class="sec-title">학력</div>
    """, unsafe_allow_html=True)

    edu = [
        ("2017 — 2021", "○○대학교 컴퓨터공학과", "학점 3.9 / 4.5 졸업"),
        ("2014 — 2017", "○○고등학교",           "이과 졸업"),
    ]
    for period, school, detail in edu:
        st.markdown(f"""
        <div class="tl-item">
            <div class="tl-dot gray"></div>
            <div>
                <span class="tl-period gray">{period}</span>
                <div class="tl-title">{school}</div>
                <div class="tl-sub">{detail}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-card">
        <div class="sec-label">INTERESTS</div>
        <div class="sec-title">관심 분야</div>
    """, unsafe_allow_html=True)

    for item in ["⚡ 에너지 데이터 분석", "🤖 AI / ML 응용", "📱 서비스 UX · UI", "☁️ 클라우드 아키텍처", "🌿 탄소중립 IT"]:
        st.markdown(f'<div class="int-chip">{item}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  프로젝트
# ══════════════════════════════════════════════
st.markdown("""
<div class="sec-label">WORKS</div>
<div class="sec-title" style="font-size:1.5rem;">주요 프로젝트</div>
""", unsafe_allow_html=True)

projects = [
    ("⚡", "KDN Charge — EV 충전 운영 시스템",
     "전국 200개소 충전소 실시간 모니터링 · 운영. Supabase 기반 풀스택 개발.",
     ["HTML/CSS/JS", "Supabase", "Realtime"], True),
    ("📊", "전력 설비 이상 탐지 대시보드",
     "센서 데이터 기반 이상 징후 조기 탐지. ML 모델을 Streamlit으로 시각화.",
     ["Python", "Streamlit", "Scikit-learn"], False),
    ("🤖", "사내 보고서 자동화",
     "주간 KPI 리포트 자동 생성·배포. 수작업 4시간 → 5분으로 단축.",
     ["Python", "Airflow", "Slack API"], False),
    ("🏛️", "DR 스케줄링 최적화 PoC",
     "DR 이벤트 발생 시 충전소 부하 자동 조절 최적화 알고리즘 프로토타입.",
     ["Python", "OR-Tools", "REST API"], True),
]

p1, p2 = st.columns(2, gap="large")
for i, (icon, name, desc, tags, is_red) in enumerate(projects):
    col = p1 if i % 2 == 0 else p2
    with col:
        tags_html = "".join(
            f'<span class="proj-tag{"  red-tag" if j == 0 and is_red else ""}">{t}</span>'
            for j, t in enumerate(tags)
        )
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-icon">{icon}</div>
            <div class="proj-name">{name}</div>
            <div class="proj-desc">{desc}</div>
            <div>{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  CTA
# ══════════════════════════════════════════════
st.markdown("""
<div class="cta-wrap">
    <div class="cta-title">같이 <em>만들어요</em> ●</div>
    <div class="cta-sub">새로운 아이디어, 협업 제안, 기술 토론 언제든지 환영합니다.</div>
    <span class="cta-email">📧 honghyelim.22@kdn.com</span>
</div>
<div class="footer-note">© 2026 Hong Hye Rim · Built with Streamlit</div>
""", unsafe_allow_html=True)
