// MODIFIED START - DiagnosticForm.tsx
import React, { useState } from 'react';

interface InputData {
  currentMRR: number; // 현재 월 반복 매출 (Monthly Recurring Revenue)
  operationalHoursPerMonth: number; // 운영 시간 (시간/월)
  criticalFailureRate: number; // 핵심 실패율 (%)
}

// 가짜 API 호출 함수 (실제로는 FastAPI 백엔드 연동 예정)
const calculateFailureCost = async (data: InputData): Promise<number> => {
  console.log("API Mock Call: Calculating Failure Cost...");
  await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate network delay

  // [근거: 지난 의사결정 로그] - 실패 비용은 재무적 손실과 연결됨.
  // 가짜 계산 로직: (MRR * Failure Rate) + (Hours * Penalty Factor)
  const failureCost = data.currentMRR * (data.criticalFailureRate / 100) * 5; // 단순화된 비즈니스 논리
  return Math.round(failureCost);
};

/**
 * 사용자의 핵심 시스템 데이터를 받아 Failure Cost를 진단하고 표시하는 컴포넌트.
 */
const DiagnosticForm: React.FC = () => {
  const [formData, setFormData] = useState<InputData>({
    currentMRR: 0,
    operationalHoursPerMonth: 160,
    criticalFailureRate: 5, // 기본값 설정 (5%)
  });
  const [failureCost, setFailureCost] = useState<number | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: parseFloat(value) || 0,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.currentMRR || !formData.criticalFailureRate) return;

    setIsLoading(true);
    setFailureCost(null);

    try {
      // 🚨 중요: 실제 API 호출 로직이 들어갈 자리입니다.
      const cost = await calculateFailureCost(formData);
      setFailureCost(cost);
    } catch (error) {
      console.error("Diagnosis failed:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-6 border border-[#E74C3C] bg-red-50/50 shadow-xl">
      <h2 className="text-2xl font-bold mb-4 text-[#E74C3C]">🚨 System Audit: Failure Cost 진단</h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="mrr" className="block text-sm font-medium text-gray-700 mb-1">
            현재 월 반복 매출 (MRR) <span className="text-red-500">*</span>
          </label>
          <input
            type="number"
            name="currentMRR"
            id="mrr"
            onChange={handleChange}
            value={formData.currentMRR}
            onChange={handleChange}
            className="w-full p-3 border rounded focus:ring-[#FF6B3D] focus:border-[#FF6B3D]"
            placeholder="예: 10,000"
            required
          />
        </div>
        <div>
          <label htmlFor="hours" className="block text-sm font-medium text-gray-700 mb-1">
            월간 운영 가능 시간 (시간)
          </label>
          <input
            type="number"
            name="operationalHoursPerMonth"
            id="hours"
            onChange={handleChange}
            value={formData.operationalHoursPerMonth}
            className="w-full p-3 border rounded focus:ring-[#FF6B3D] focus:border-[#FF6B3D]"
          />
        </div>
        <div>
          <label htmlFor="failureRate" className="block text-sm font-medium text-gray-700 mb-1">
            핵심 시스템 실패율 (예상치 %) <span className="text-red-500">*</span>
          </label>
          <input
            type="number"
            name="criticalFailureRate"
            id="failureRate"
            onChange={handleChange}
            value={formData.criticalFailureRate}
            className="w-full p-3 border rounded focus:ring-[#FF6B3D] focus:border-[#FF6B3D]"
            placeholder="예: 5"
            required
          />
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className={`w-full py-3 rounded text-white font-bold transition duration-200 ${
            isLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-[#FF6B3D] hover:bg-[#E74C3C]'
          }`}
        >
          {isLoading ? '진단 중... 잠시만 기다려 주세요.' : '실패 비용 진단 시작'}
        </button>

        {failureCost !== null && (
          <div className="mt-8 p-6 bg-[#FFEBEE] border-l-4 border-[#E74C3C] shadow-md">
            <h3 className="text-xl font-bold text-[#E74C3C]">⚠️ 진단 완료: 예상 실패 비용</h3>
            <p className="text-5xl font-extrabold mt-2">{`$${failureCost.toLocaleString()}`}
              </p>
            <p className="text-lg text-gray-600">
              이 금액은 현재 시스템 구조적 결함으로 인해 예상되는 잠재적 재정 손실액입니다. 
              이 수치가 바로 System Audit의 근거가 됩니다.
            </p>
          </div>
        )}
      </form>
    </div>
  );
};

export default DiagnosticForm;
// MODIFIED END - DiagnosticForm.tsx