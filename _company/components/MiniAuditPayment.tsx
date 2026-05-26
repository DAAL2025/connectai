// MODIFIED START - MiniAuditPayment.tsx
import React, { useState } from 'react';

interface PaymentState {
  isProcessing: boolean;
}

/**
 * 실패 비용 진단 결과 직후, 고객의 다음 액션을 유도하는 Mockup 결제 모듈.
 */
const MiniAuditPayment: React.FC = () => {
  const [paymentData, setPaymentData] = useState({ name: '', email: '' });
  const [state, setState] = useState<PaymentState>({ isProcessing: false });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPaymentData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handlePaymentSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!paymentData.email || !paymentData.name) return;

    setState({ isProcessing: true });
    console.log("Mock Payment Call: Attempting Mini-Audit purchase...");
    await new Promise(resolve => setTimeout(resolve, 1500)); // Simulate payment processing delay

    // 실제 PG 연동 로직 (Stripe/PayPal SDK)이 들어갈 자리입니다.
    alert(`✅ 성공적으로 Mini-Audit을 신청했습니다! (${paymentData.email})`);
    setState({ isProcessing: false });
  };

  return (
    <div className="p-8 bg-gray-50 border border-[#FF6B3D]/50 rounded-xl shadow-lg mt-12">
      <h2 className="text-3xl font-bold mb-4 text-center text-red-700">🚀 다음 단계: Mini-Audit (Small Win)</h2>
      <p className="text-center mb-6 text-gray-700">
        진단된 실패 비용을 줄이는 첫걸음. $99 상당의 시스템 기초 진단을 받아보세요.
      </p>

      <div className="max-w-md mx-auto space-y-4">
        {/* 가격 정보 섹션 */}
        <div className="bg-[#FF6B3D] text-white p-6 rounded-lg text-center shadow-xl transform scale-105">
          <p className="text-sm opacity-80">단일 결제</p>
          <h3 className="text-4xl font-extrabold mt-1">$99</h3>
          <p className="text-sm mt-2">(System Foundation Mini-Audit)</p>
        </div>

        {/* 폼 */}
        <form onSubmit={handlePaymentSubmit} className="space-y-4 p-6 bg-white border rounded-lg shadow-inner">
            <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">이름</label>
                <input
                    type="text"
                    name="name"
                    id="name"
                    onChange={handleInputChange}
                    className="w-full p-3 border rounded focus:ring-[#FF6B3D] focus:border-[#FF6B3D]"
                    placeholder="이름을 입력하세요."
                    required
                />
            </div>
            <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">비즈니스 이메일</label>
                <input
                    type="email"
                    name="email"
                    id="email"
                    onChange={handleInputChange}
                    className="w-full p-3 border rounded focus:ring-[#FF6B3D] focus:border-[#FF6B3D]"
                    placeholder="your@company.com"
                    required
                />
            </div>

            <button
              type="submit"
              disabled={state.isProcessing}
              className={`w-full py-3 rounded text-white font-bold transition duration-200 ${
                state.isProcessing ? 'bg-gray-400 cursor-not-allowed' : 'bg-[#E74C3C] hover:bg-red-600'
              }`}
            >
              {state.isProcessing ? '결제 처리 중... 💳' : 'Mini-Audit 결제 및 보고서 요청하기'}
            </button>
        </form>

      </div>
    </div>
  );
};

export default MiniAuditPayment;
// MODIFIED END - MiniAuditPayment.tsx