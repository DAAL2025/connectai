// Next.js API 라우트 또는 서버 컴포넌트에서 사용할 핵심 인터페이스 및 스켈레톤 정의
import { AlertCardSchema, AlertStatus } from '../types/alertCard';

/**
 * Alert Card 데이터베이스 인터페이스 (실제로는 DB 쿼리로 대체됨)
 */
export interface AlertData {
  id: string;
  title: string;
  severity: AlertCardSchema['severity'];
  message: string;
  timestamp: string;
  actionSteps: string[];
}

/**
 * API 스켈레톤 함수 정의 (실제 구현은 DB 레이어에 의존)
 */
export const alertCardService = {
  /**
   * 새로운 Alert Card를 생성합니다.
   * @param data 신규 카드 데이터
   * @returns 생성된 데이터
   */
  createAlert: async (data: Omit<AlertData, 'id'>): Promise<AlertData> => {
    console.log("API Skeleton: createAlert 호출됨. 데이터 검증 필요.");
    // TODO: 실제 DB 삽입 로직 구현 필요
    const newId = 'mock-' + Date.now();
    return { ...data, id: newId };
  },

  /**
   * 특정 Alert Card를 조회합니다.
   * @param id 조회할 카드 ID
   * @returns 카드 데이터 또는 에러
   */
  getAlert: async (id: string): Promise<AlertData | null> => {
    console.log(`API Skeleton: getAlert(${id}) 호출됨.`);
    // TODO: 실제 DB 조회 로직 구현 필요
    return null; // 임시 반환
  },

  /**
   * 카드 상태를 업데이트합니다. (예: 해결 처리)
   * @param id 카드 ID
   * @param status 새로운 상태 ('active', 'resolved' 등)
   * @returns 업데이트된 데이터
   */
  updateAlertStatus: async (id: string, status: AlertStatus): Promise<AlertData> => {
    console.log(`API Skeleton: updateAlertStatus(${id}, ${status}) 호출됨.`);
    // TODO: 실제 DB 업데이트 로직 구현 필요
    return { id, title: "Updated Title", severity: 'Normal', message: "Status updated successfully" };
  }
};