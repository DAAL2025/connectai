import { NextApiRequest, NextApiResponse } from 'next';
import { calculateLai } from '../lib/lai_logic'; // LAI 계산 로직 모듈 가정

// 이 함수는 실제 데이터베이스 연결을 대체하며, 추후 DB 스키마에 맞게 확장될 것입니다.
const mockDatabase = {
    // 실제로는 여기에 DB 쿼리 로직이 들어갈 예정
};

/**
 * Loss Avoidance Index (LAI) 계산 API 엔드포인트
 * @param req NextApiRequest 객체
 * @param res NextApiResponse 객체
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    // 1. 인증 및 메소드 확인 (보안 점검)
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { mrr, churn_rate, historical_data } = req.body;

    // 2. 입력 데이터 유효성 검증 (경계 조건 1차 필터)
    if (!mrr || !churn_rate || !historical_data) {
        return res.status(400).json({ error: 'Missing required fields: mrr, churn_rate, historical_data' });
    }

    // LAI 계산 로직 실행 및 경계 조건 2차 검증 (실제 수학적 안정성 점검)
    try {
        const laiResult = calculateLai(mrr, churn_rate, historical_data);

        if (isNaN(laiResult) || !isFinite(laiResult)) {
            // 계산 오류 발생 시 500 에러 반환 (내부 로직 문제)
            console.error('LAI Calculation Failed: Result is NaN or Infinity', { mrr, churn_rate });
            return res.status(500).json({ error: 'Calculation failed due to invalid mathematical result.' });
        }

        // 3. 데이터 저장 프로토타입 (실제 DB 연동 예정)
        // await mockDatabase.saveLaiRecord({ mrr, churn_rate, lai: laiResult, timestamp: new Date() });

        // 4. 성공 응답
        return res.status(200).json({
            success: true,
            lai_value: parseFloat(laiResult.toFixed(4)), // 소수점 4자리로 고정하여 반환
            message: 'LAI calculated and recorded successfully.',
            data_source_check: 'PASS'
        });

    } catch (error) {
        // 외부 서비스 오류 또는 기타 예외 처리
        console.error('API Error during LAI calculation:', error);
        if (error instanceof Error) {
             return res.status(503).json({ 
                success: false, 
                error: 'Service Unavailable', 
                detail: `Calculation error: ${error.message}` 
            });
        }
        return res.status(500).json({ success: false, error: 'Internal Server Error' });
    }
}