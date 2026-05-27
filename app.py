import streamlit as st

st.set_page_config(
    page_title="홍혜림 | 자기소개",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 전역 스타일 ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

/* 헤더 여백 제거 */
.block-container { padding-top: 2rem; padding-bottom: 3rem; }

/* 섹션 카드 */
.section-card {
    background: #f8f9fc;
    border-radius: 16px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.2rem;
    border: 1px solid #eee;
}

/* 히어로 */
.hero-wrap {
    background: linear-gradient(135deg, #0a0c1e 0%, #0d1f3c 60%, #0a2a1e 100%);
    border-radius: 20px;
    padding: 3rem 2.5rem;
    color: #fff;
    margin-bottom: 2rem;
}
.hero-name {
    font-size: 2.8rem;
    font-weight: 900;
    margin: 0 0 0.3rem;
    letter-spacing: -0.02em;
}
.hero-title {
    font-size: 1.1rem;
    color: #00c896;
    font-weight: 700;
    margin-bottom: 1rem;
}
.hero-desc {
    font-size: 0.95rem;
    color: rgba(255,255,255,0.75);
    line-height: 1.8;
    max-width: 520px;
}
.hero-tag {
    display: inline-block;
    background: rgba(0,200,150,0.15);
    border: 1px solid rgba(0,200,150,0.4);
    color: #00c896;
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 0.8rem;
    font-weight: 700;
    margin: 0.3rem 0.3rem 0 0;
}
.avatar-circle {
    width: 120px; height: 120px;
    border-radius: 50%;
    background: linear-gradient(135deg, #00c896, #0d6efd);
    display: flex; align-items: center; justify-content: center;
    font-size: 3.2rem;
    border: 4px solid rgba(255,255,255,0.2);
    margin: 0 auto;
}
.contact-pill {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 0.85rem;
    color: rgba(255,255,255,0.85);
    margin: 0.3rem 0.3rem 0 0;
}

/* 섹션 제목 */
.sec-title {
    font-size: 1.15rem;
    font-weight: 900;
    color: #1a1a2e;
    margin: 0 0 1.2rem;
    display: flex; align-items: center; gap: 8px;
}
.sec-title::after {
    content:'';
    flex: 1;
    height: 2px;
    background: linear-gradient(to right, #00c896, transparent);
    border-radius: 2px;
}

/* 스킬 바 */
.skill-wrap { margin-bottom: 0.75rem; }
.skill-label {
    display: flex; justify-content: space-between;
    font-size: 0.88rem; font-weight: 600; color: #333;
    margin-bottom: 5px;
}
.skill-bar-bg {
    height: 8px; background: #e8ecf0; border-radius: 100px; overflow: hidden;
}
.skill-bar-fill {
    height: 100%; border-radius: 100px;
    background: linear-gradient(90deg, #00c896, #0d9068);
    transition: width 0.6s ease;
}
.skill-bar-fill.blue { background: linear-gradient(90deg, #3b82f6, #1d4ed8); }
.skill-bar-fill.purple { background: linear-gradient(90deg, #8b5cf6, #6d28d9); }
.skill-bar-fill.orange { background: linear-gradient(90deg, #f59e0b, #d97706); }

/* 타임라인 */
.timeline-item {
    display: flex; gap: 1rem;
    margin-bottom: 1.2rem;
    position: relative;
}
.timeline-dot {
    width: 14px; height: 14px; border-radius: 50%;
    background: #00c896;
    flex-shrink: 0;
    margin-top: 5px;
    position: relative; z-index: 1;
}
.timeline-item:not(:last-child)::before {
    content: '';
    position: absolute;
    left: 6px; top: 18px;
    width: 2px;
    height: calc(100% + 4px);
    background: #e0f5ee;
}
.timeline-period {
    font-size: 0.78rem; font-weight: 700;
    color: #00a87a;
    background: #e8faf3;
    padding: 2px 10px;
    border-radius: 100px;
    display: inline-block;
    margin-bottom: 4px;
}
.timeline-title { font-size: 0.97rem; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
.timeline-sub { font-size: 0.84rem; color: #888; }

/* 프로젝트 카드 */
.proj-card {
    background: #fff;
    border: 1px solid #eee;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
    transition: box-shadow 0.2s;
}
.proj-card:hover { box-shadow: 0 4px 16px rgba(0,200,150,0.1); border-color: #b0edd8; }
.proj-name { font-size: 0.97rem; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
.proj-desc { font-size: 0.85rem; color: #666; line-height: 1.6; margin-bottom: 8px; }
.proj-tag {
    display: inline-block;
    background: #f0f8f4; color: #00a87a;
    border-radius: 6px; padding: 2px 8px;
    font-size: 0.75rem; font-weight: 700;
    margin: 2px 2px 0 0;
}

/* 통계 숫자 */
.stat-box {
    text-align: center;
    background: linear-gradient(135deg, #0a0c1e, #0d1f3c);
    border-radius: 14px;
    padding: 1.4rem 0.8rem;
    color: #fff;
}
.stat-num { font-size: 2.2rem; font-weight: 900; color: #00c896; display: block; }
.stat-lbl { font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 2px; }
</style>
""", unsafe_allow_html=True)


# ── 히어로 섹션 ──────────────────────────────────────────────
col_av, col_info = st.columns([1, 3], gap="large")

with col_av:
    st.markdown("""
    <div style="display:flex;align-items:center;justify-content:center;height:100%;padding-top:0.5rem;">
        <div class="avatar-circle">👩‍💻</div>
    </div>
    """, unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div class="hero-wrap">
        <p class="hero-title">Data Engineer · Full-Stack Developer</p>
        <h1 class="hero-name">홍 혜 림</h1>
        <p class="hero-desc">
            데이터와 코드로 문제를 해결하는 개발자입니다.<br>
            전력 에너지 분야의 디지털 전환을 위한 시스템을 기획·개발하며,<br>
            사용자 중심의 직관적인 서비스를 만드는 것을 좋아합니다.
        </p>
        <div style="margin-top:1.2rem;">
            <span class="hero-tag">⚡ 에너지 IT</span>
            <span class="hero-tag">🐍 Python</span>
            <span class="hero-tag">📊 데이터 분석</span>
            <span class="hero-tag">🌐 웹 개발</span>
            <span class="hero-tag">☁️ 클라우드</span>
        </div>
        <div style="margin-top:1.4rem;">
            <span class="contact-pill">📧 honghyelim.22@kdn.com</span>
            <span class="contact-pill">🏢 KDN (한국전력기술)</span>
            <span class="contact-pill">📍 서울, 대한민국</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── 요약 통계 ──────────────────────────────────────────────
st.markdown("---")
s1, s2, s3, s4 = st.columns(4)
stats = [
    ("3+", "년 개발 경력"),
    ("15+", "완료 프로젝트"),
    ("5+", "기술 스택"),
    ("100%", "열정 지수"),
]
for col, (num, lbl) in zip([s1, s2, s3, s4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <span class="stat-num">{num}</span>
            <span class="stat-lbl">{lbl}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── 본문 2단 레이아웃 ──────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

# ── 왼쪽: 기술 스택 ──
with left:
    st.markdown('<div class="sec-title">🛠 기술 스택</div>', unsafe_allow_html=True)

    skills = [
        ("Python",          92, ""),
        ("SQL / PostgreSQL", 85, ""),
        ("Streamlit",        88, ""),
        ("JavaScript / HTML", 78, "blue"),
        ("Git / GitHub",     83, "blue"),
        ("Docker / Linux",   70, "purple"),
        ("데이터 분석 (Pandas/Numpy)", 87, ""),
        ("AWS / Supabase",   72, "orange"),
    ]
    for name, pct, color_cls in skills:
        st.markdown(f"""
        <div class="skill-wrap">
            <div class="skill-label"><span>{name}</span><span>{pct}%</span></div>
            <div class="skill-bar-bg">
                <div class="skill-bar-fill {color_cls}" style="width:{pct}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 자격증
    st.markdown('<div class="sec-title">🏅 자격증 / 수료</div>', unsafe_allow_html=True)
    certs = [
        ("정보처리기사", "한국산업인력공단", "2023"),
        ("ADsP (데이터분석준전문가)", "한국데이터산업진흥원", "2022"),
        ("SQL 개발자(SQLD)", "한국데이터산업진흥원", "2022"),
        ("클라우드 컴퓨팅 과정 수료", "AWS Training", "2024"),
    ]
    for title, issuer, year in certs:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:0.6rem 0;border-bottom:1px solid #f0f0f0;">
            <span style="font-size:1.2rem;">🎖</span>
            <div>
                <div style="font-size:0.9rem;font-weight:700;color:#1a1a2e;">{title}</div>
                <div style="font-size:0.78rem;color:#888;">{issuer} · {year}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── 오른쪽: 경력 + 학력 ──
with right:
    st.markdown('<div class="sec-title">💼 경력</div>', unsafe_allow_html=True)

    career = [
        ("2022.07 ~ 현재", "KDN (한국전력기술)", "데이터 엔지니어 · IT전략팀",
         "전력 설비 운영 데이터 분석 시스템 개발, 사내 디지털 전환(DX) 과제 수행"),
        ("2021.01 ~ 2022.06", "스타트업 A사", "풀스택 개발자 (인턴 → 정직원)",
         "사용자 대시보드 및 REST API 개발, Python 백엔드 설계"),
    ]
    for period, company, role, desc in career:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div>
                <span class="timeline-period">{period}</span>
                <div class="timeline-title">{company}</div>
                <div class="timeline-sub" style="font-weight:600;color:#555;margin-bottom:3px;">{role}</div>
                <div class="timeline-sub">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="sec-title">🎓 학력</div>', unsafe_allow_html=True)
    edu = [
        ("2017.03 ~ 2021.02", "○○대학교", "컴퓨터공학과 졸업 (학점 3.9/4.5)"),
        ("2014.03 ~ 2017.02", "○○고등학교", "이과 졸업"),
    ]
    for period, school, detail in edu:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#3b82f6;"></div>
            <div>
                <span class="timeline-period" style="color:#3b82f6;background:#eff6ff;">{period}</span>
                <div class="timeline-title">{school}</div>
                <div class="timeline-sub">{detail}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="sec-title">🌱 관심 분야</div>', unsafe_allow_html=True)
    interests = ["⚡ 에너지 데이터 분석", "🤖 AI/ML 활용", "📱 서비스 UX/UI",
                 "☁️ 클라우드 아키텍처", "🌿 탄소중립 IT"]
    cols = st.columns(2)
    for i, item in enumerate(interests):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background:#f0fdf4;border:1px solid #d0f0e0;border-radius:10px;
                        padding:0.6rem 1rem;margin-bottom:0.5rem;font-size:0.88rem;
                        font-weight:600;color:#1a1a2e;">
                {item}
            </div>
            """, unsafe_allow_html=True)


# ── 프로젝트 ──────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="sec-title">🚀 주요 프로젝트</div>', unsafe_allow_html=True)

projects = [
    {
        "name": "KDN Charge — EV 충전 운영 시스템",
        "desc": "전국 200개소 전기차 충전소 실시간 모니터링 및 운영 관리 시스템. 대민 홈페이지, 운영 어드민, Supabase 연동까지 풀스택 개발.",
        "tags": ["HTML/CSS/JS", "Supabase", "GitHub Pages", "Realtime"],
        "icon": "⚡",
    },
    {
        "name": "전력 설비 이상 탐지 대시보드",
        "desc": "센서 데이터 기반 전력 설비 이상 징후 조기 탐지 시스템. 머신러닝 모델을 Streamlit 대시보드로 시각화.",
        "tags": ["Python", "Streamlit", "Scikit-learn", "Pandas"],
        "icon": "📊",
    },
    {
        "name": "사내 데이터 보고서 자동화",
        "desc": "주간 KPI 리포트를 자동 생성·배포하는 파이프라인 구축. 수작업 4시간을 자동화 5분으로 단축.",
        "tags": ["Python", "Airflow", "PostgreSQL", "Slack API"],
        "icon": "🤖",
    },
    {
        "name": "DR (수요반응) 스케줄링 최적화 PoC",
        "desc": "국민DR·플러스DR 이벤트 발생 시 충전소 부하를 자동 조절하는 스케줄링 알고리즘 프로토타입 개발.",
        "tags": ["Python", "OR-Tools", "REST API"],
        "icon": "🏛️",
    },
]

p_cols = st.columns(2)
for i, p in enumerate(projects):
    with p_cols[i % 2]:
        tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
        st.markdown(f"""
        <div class="proj-card">
            <div style="font-size:1.8rem;margin-bottom:6px;">{p["icon"]}</div>
            <div class="proj-name">{p["name"]}</div>
            <div class="proj-desc">{p["desc"]}</div>
            <div>{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)


# ── 연락처 ──────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="background:linear-gradient(135deg,#0a0c1e,#0d1f3c);border-radius:20px;
            padding:2.5rem;text-align:center;color:#fff;">
    <div style="font-size:2rem;margin-bottom:0.5rem;">📬</div>
    <h3 style="font-weight:900;font-size:1.5rem;margin-bottom:0.5rem;">함께 만들어요</h3>
    <p style="color:rgba(255,255,255,0.7);font-size:0.95rem;margin-bottom:1.5rem;">
        새로운 아이디어, 협업 제안, 기술 토론 언제든지 환영합니다.
    </p>
    <div style="display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;">
        <span style="background:rgba(0,200,150,0.15);border:1px solid rgba(0,200,150,0.4);
                     color:#00c896;border-radius:10px;padding:10px 20px;font-weight:700;font-size:0.9rem;">
            📧 honghyelim.22@kdn.com
        </span>
        <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);
                     color:rgba(255,255,255,0.85);border-radius:10px;padding:10px 20px;font-weight:700;font-size:0.9rem;">
            🏢 KDN 한국전력기술
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#bbb;font-size:0.82rem;'>© 2026 홍혜림 · Built with Streamlit 🎈</p>", unsafe_allow_html=True)
