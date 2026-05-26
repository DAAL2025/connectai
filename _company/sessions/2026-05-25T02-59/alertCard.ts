import React, { useState, useEffect, useCallback } from 'react';

// 1. 데이터 모델 정의 (Designer의 데이터 모델 기반)
interface AlertData {
  id: string;
  level: 'critical' | 'warning' | 'info';
  title: string; // What (문제)
  cause: string; // Why (원인)
  impact: number; // 재무적 영향 예상치
  visualizationData: any; // 그래프 데이터 등 시각화에 필요한 데이터
  actionSteps: string[]; // Action Step (해결 방안)
  status: 'pending' | 'resolved' | 'acknowledged';
  timestamp: string;
}

interface AlertCardProps {
  alert: AlertData;
  onActionClick: (actionStep: string) => void; // CTA 클릭 핸들러
  isLoading: boolean;
  error: string | null; // API 호출 실패 등 에러 상태
}

// 2. 핵심 컴포넌트 구현
const AlertCard: React.FC<AlertCardProps> = ({ alert, onActionClick, isLoading, error }) => {
  const [localStatus, setLocalStatus] = useState(alert.status);

  // 데이터 로딩 및 상태 초기화 로직 (시스템 통합 안정성 확보)
  useEffect(() => {
    if (error) {
      setLocalStatus('error');
      console.error(`AlertCard Data Load Error for ID ${alert.id}:`, error);
      return;
    }
    // 데이터가 성공적으로 로드되면 상태를 초기화하거나 최종 상태로 설정
    setLocalStatus(alert.status);
  }, [alert.id, alert.status, error]);

  // 액션 버튼 핸들러 (워크플로우 트리거)
  const handleAction = useCallback((actionStep: string) => {
    console.log(`Action Triggered for Alert ${alert.id}: ${actionStep}`);
    // 실제 시스템 호출 로직은 상위 컴포넌트나 API로 위임되어야 함 (시스템 통합 안전장치)
    onActionClick(actionStep);
  }, [alert.id, onActionClick]);

  // 3. UI 렌더링 및 오류 처리 (보안성 확보)
  const cardClasses = {
    critical: 'bg-red-100 border-red-500 text-red-800',
    warning: 'bg-yellow-100 border-yellow-500 text-yellow-800',
    info: 'bg-blue-100 border-blue-500 text-blue-800',
    error: 'bg-red-50 border-red-300 text-red-700',
  };

  const statusClass = cardClasses[alert.level] || cardClasses.info;

  return (
    <div className={`p-6 mb-4 border-l-4 shadow-md transition duration-300 ${statusClass}`}>
      {/* 헤더 영역: 엠블럼 및 제목 */}
      <div className="flex justify-between items-start mb-3">
        <span className={`font-bold text-lg tracking-wider uppercase`}>
          {alert.level} Alert
        </span>
        <span className="text-sm font-semibold">{alert.id}</span>
      </div>

      {/* 핵심 메시지 영역 (What & Why) */}
      <h2 className="text-xl font-bold mb-2">{alert.title}</h2>
      <p className="text-gray-700 mb-4 border-b pb-3">
        <strong>원인 (Why):</strong> {alert.cause}
      </p>

      {/* 시각화 및 재무 영향 */}
      <div className="mb-4">
        <p className="text-sm font-medium mb-1">재무적 영향 예상치:</p>
        <span className={`font-extrabold text-2xl ${alert.impact > 0 ? 'text-red-600' : 'text-green-600'}`}>
          ${alert.impact.toLocaleString()}
        </span>
      </div>

      {/* 상세 정보 및 액션 유도 영역 (Action Step) */}
      <div className="mt-4 pt-3 border-t">
        <p className="font-semibold mb-2">액션 단계:</p>
        <ul className="list-disc list-inside text-sm space-y-1 mb-4">
          {alert.actionSteps.map((step, index) => (
            <li key={index} className="text-gray-600">{step}</li>
          ))}
        </ul>

        {/* CTA 버튼: 시스템 통합 및 안전장치 적용 */}
        <button
          onClick={() => handleAction(alert.actionSteps[0])} // 첫 번째 액션 단계로 트리거
          disabled={isLoading || localStatus === 'resolved'}
          className={`w-full py-2 px-4 rounded font-semibold transition duration-150 ${
            localStatus === 'resolved' ? 'bg-gray-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700 text-white'
          }`}
        >
          {isLoading ? '처리 중...' : `다음 단계 시작 (${alert.actionSteps[0]})`}
        </button>

        {/* 에러 및 상태 표시 (최종 검증) */}
        {error && (
          <p className="mt-3 text-sm font-medium text-red-600">
            ⚠️ 시스템 오류: {error} (데이터 통합 실패)</p>
        )}
        {!error && (
             <p className="mt-3 text-xs text-gray-500">
                현재 상태: {localStatus.toUpperCase()}
            </p>
        )}
      </div>
    </div>
  );
};

export default AlertCard;