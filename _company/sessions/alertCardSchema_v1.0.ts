/**
 * Alert Card System Data Model Interface
 * Designer의 Mock-up 및 Business 데이터 흐름을 반영한 핵심 타입 정의
 */

export interface AlertCardSchema {
  id: string; // 고유 ID (UUID 권장)
  level: 'critical' | 'warning' | 'info'; // 알림 레벨 (Alert Level)
  title: string; // 카드 제목 (Card Title)
  problemCause: string; // 문제의 원인 (Problem Cause - Pain Point 강조)
  impactMetrics: Record<string, number>; // 재무적 영향 예상치 또는 지표 그래프 데이터 (Impact Metrics)
  actionSteps: string[]; // 해결을 위한 구체적인 액션 단계 (Action Steps)
  status: 'open' | 'in_progress' | 'resolved'; // 현재 상태 (Status)
  createdAt: Date; // 생성 시간
  updatedAt: Date; // 최종 업데이트 시간
  dataFlowId?: string; // 데이터 흐름 ID (선택적, 시스템 연동용)
}

export interface ApiRequest {
  type: 'create' | 'update'; // 요청 유형
  data: AlertCardSchema; // 전달할 데이터 객체
}

export interface ApiResponse {
  success: boolean;
  message: string;
  data?: AlertCardSchema; // 성공 시 반환될 데이터
  error?: string; // 실패 시 에러 메시지
}

// API 엔드포인트 스켈레톤 정의 (Next.js API Route 기준)
export const apiEndpoints = {
    createAlertCard: {
        method: 'POST',
        path: '/api/alerts',
        description: "새로운 Alert Card를 생성합니다."
    },
    getAlertCards: {
        method: 'GET',
        path: '/api/alerts',
        description: "모든 Alert Card 목록을 조회합니다."
    },
    updateAlertCard: {
        method: 'PUT',
        path: '/api/alerts/:id',
        description: "특정 Alert Card를 업데이트합니다."
    }
};