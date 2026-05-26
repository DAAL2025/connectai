// MODIFIED START - SystemAuditPage.tsx
import React from 'react';
import DiagnosticForm from '../components/DiagnosticForm';
import MiniAuditPayment from '../components/MiniAuditPayment';

/**
 * 최종 랜딩 페이지: Failure Cost 진단부터 구매 전환까지의 전체 흐름을 담은 MVP 페이지.
 */
const SystemAuditPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-8 sm:p-16">
      {/* Hero Section - 문제 인식 극대화 */}
      <header className="text-center py-20 border-b mb-12">
        <h1 className="text-6xl font-extrabold text-gray-900 tracking-tight">
          운영 시스템의 숨겨진 리스크를 찾아드립니다.
        </h1>
        <p className="mt-4 max-w-3xl mx-auto text-xl text-gray-600">
          단순한 웹사이트 구축이 아닌, **예측 가능한 매출 흐름(MRR)을 설계하고 자동화하는 운영 시스템**으로 전환해야 합니다. 실패 비용 진단을 통해 지금 당장 막아야 할 손실액을 확인하세요.
        </p>
      </header>

      <main className="max-w-4xl mx-auto space-y-16">
        {/* 1단계: Failure Cost Diagnosis */}
        <section aria-labelledby="diagnosis-title">
          <h2 id="diagnosis-title" className="text-3xl font-bold mb-8 text-center text-gray-800">
            Step 1. 시스템 진단: 실패 비용(Failure Cost) 계산
          </h2>
          <DiagnosticForm />
        </section>

        {/* 2단계: Mini-Audit CTA (구매 유도) */}
        <section aria-labelledby="mini-audit-title">
          <h2 id="mini-audit-title" className="text-3xl font-bold mb-8 text-center text-gray-800 mt-16">
            Step 2. 손실 비용 해결: System Audit Mini-Audit 신청하기
          </h2>
          <MiniAuditPayment />
        </section>

      </main>

      {/* Footer / CTA Reminder */}
      <footer className="text-center py-10 mt-20 border-t">
        <p className="text-xl text-gray-500">
          지금 바로 진단하여, 당신의 비즈니스가 겪고 있는 구조적 손실을 최소화하세요.
        </p>
      </footer>
    </div>
  );
};

export default SystemAuditPage;
// MODIFIED END - SystemAuditPage.tsx