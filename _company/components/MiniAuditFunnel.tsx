// /volumes/daal/documents/01.work/connect ai/_company/components/MiniAuditFunnel.tsx
import React, { useState, useCallback } from 'react';

interface AuditResult {
  fcAmount: number;
  warningLevel: 'CRITICAL' | 'HIGH' | 'LOW';
  message: string;
}

// 초기 상태 정의
const initialAuditState = { fcAmount: 0, warningLevel: 'LOW', message: "데이터를 입력하여 구조적 결함을 진단해보세요." };


export const MiniAuditFunnel: React.FC = () => {
  // 사용자 입력 state (가정)
  const [formData, setFormData] = useState({
    featureA: 50, // 예시 데이터
    featureB: 30,
    userInteractionScore: 80,
  });

  // API 호출 및 상태 업데이트 로직
  const handleAuditSubmit = useCallback(async (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Initiating audit calculation...");

    try {
      // Next.js API Endpoint 호출 (실제 백엔드와 연결되는 부분)
      const response = await fetch('/api/v1/audit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`API Call Failed: ${response.statusText}`);
      }

      const data: AuditResult = await response.json();
      // 상태 업데이트 (실시간 피드백 제공)
      console.log("Audit Successful:", data);
      // 실제 앱에서는 Context/Redux를 통해 전역 상태 관리 필요
    } catch (error) {
      console.error('Error fetching audit results:', error);
      alert('진단 실패: 서버 연결 또는 입력값이 유효하지 않습니다.');
    }
  }, [formData]);

  // UI 렌더링 로직
  const getLevelStyles = (level: 'CRITICAL' | 'HIGH' | 'LOW') => {
    switch (level) {
      case 'CRITICAL': return 'bg-red-600 border-red-800 text-white';
      case 'HIGH': return 'bg-yellow-500 border-yellow-700 text-gray-900';
      case 'LOW': return 'bg-green-100 border-green-400 text-green-800';
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-8 bg-white shadow-lg rounded-xl">
      <h1 className="text-3xl font-bold mb-6 border-b pb-2 text-red-700">Mini-Audit Funnel: 구조적 결함 진단</h1>
      <p className="mb-8 text-gray-600">당신의 웹사이트가 가진 보이지 않는 재무적 손실 비용($FC$)을 정량화하세요.</p>

      {/* 1. 입력 폼 영역 */}
      <form onSubmit={handleAuditSubmit} className="space-y-6 mb-12 p-6 border rounded-lg bg-gray-50">
        <h2 className="text-xl font-semibold text-gray-700">진단 지표 입력 (사용자 데이터)</h2>
        {/* Input Fields... */}
        <div>
          <label htmlFor="featureA" className="block text-sm font-medium text-gray-700">기능 A 완성도 점수</label>
          <input 
            type="range" id="featureA" min="0" max="100" value={formData.featureA} onChange={(e) => setFormData({...formData, featureA: parseInt(e.target.value)})} className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"/>
        </div>
        {/* ... (나머지 Input Fields 구조화 필요) */}

        <button 
          type="submit" 
          className="w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-red-700 hover:bg-red-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition duration-150"
        >
          ⚠️ $FC$ 진단 실행 (Mini-Audit 시작)
        </button>
      </form>

      {/* 2. 결과 표시 영역 */}
      <div className="p-8 border-4 rounded-xl shadow-inner" style={{ borderColor: getLevelStyles(initialAuditState.warningLevel).replace('bg-', 'border-') }}>
        <h2 className="text-2xl font-bold mb-4">📊 진단 결과</h2>

        {/* 경고 게이지 시각화 */}
        <div className={`p-5 rounded-lg text-center ${getLevelStyles(initialAuditState.warningLevel)}`}>
          <div className="text-sm uppercase tracking-widest font-bold mb-1">경고 레벨</div>
          <h3 className="text-5xl font-extrabold">$ {initialAuditState.fcAmount.toLocaleString()} KRW</h3>
          <p className="text-lg mt-2">{initialAuditState.message}</p>
        </div>

        {/* 핵심 CTA */}
        <div className="mt-8 text-center">
            <a href="/contact" className="inline-block py-3 px-10 rounded-full shadow-xl bg-red-700 hover:bg-red-800 transition duration-200 font-bold text-lg">
                구조적 결함 해소 및 컨설팅 받기 →
            </a>
        </div>
      </div>
    </div>
  );
};