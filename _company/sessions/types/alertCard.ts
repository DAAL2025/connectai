interface AlertCardSchema {
  id: string;
  title: string;
  severity: 'Normal' | 'Warning' | 'Critical';
  message: string;
  timestamp: string;
  relatedData?: Record<string, any>; // 관련 데이터는 유연하게 처리
  actionSteps: string[]; // 행동 단계 정의 (Action Flow 연동)
}

interface AlertCard {
  cardId: string;
  schema: AlertCardSchema;
  status: 'pending' | 'active' | 'resolved';
}

export type AlertStatus = 'pending' | 'active' | 'resolved';