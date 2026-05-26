# 📚 D.AAL DESIGN 산출물 저장 가이드라인 (필독)

## 📌 1. 기본 원칙: Single Source of Truth
모든 프로젝트 관련 최종 아웃풋은 `connect ai` 폴더에만 존재합니다. 로컬 데스크탑이나 임시 폴더에 파일을 보관하는 행위는 금지됩니다.

## 📂 2. 폴더 구조 (Directory Structure)
산출물 종류별로 다음의 하위 디렉토리를 활용하여 정리해 주세요.

*   `/connect ai/01_Strategy`: 기획서, 비즈니스 로드맵 등 전략 레벨 문서.
*   `/connect ai/02_Content`: 마케팅 콘텐츠(스크립트, 카피라이팅 초안) 전용 폴더. (유튜브, 인스타 산출물 저장)
*   `/connect ai/03_Design`: UI/UX 디자인 사양서, 와이어프레임 등 시각적 결과물. (디자이너 산출물 저장)
*   `/connect ai/04_Codebase`: 개발 관련 스켈레톤 코드 및 기술 명세서. (개발자 산출물 저장)
*   `/connect ai/Reports`: 최종 QA 체크리스트, 주간 보고서 등 종합 문서.

## 💾 3. 파일명 규칙 (Naming Convention)
파일 이름은 다음 포맷을 따르는 것이 가독성이 높습니다.
`YYYYMMDD_에이전트약자_산출물요약(버전)`
*예시: `20260527_sec_weeklyreport(v1)`*

## 🗑️ 4. 정리 및 아카이브 (Cleanup)
*   최종 확정된 버전은 반드시 해당 폴더의 최상단에 두고, 이전 버전 파일명에는 `_OLD`를 붙여 백업합니다.