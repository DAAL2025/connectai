import express, { Request, Response } from 'express';
import { calculateFailureCost } from '../../lib/services/failureCostService';
// Assuming a standard Express router setup

const failureCostRouter = express.Router();

/**
 * POST /api/v1/diagnostics/failure-cost
 * 진단 지표를 받아 시스템적 실패 비용(Failure Cost)을 계산합니다.
 * @param {Request} req - 요청 객체 (Body에 진단 지표 포함 예상)
 * @param {Response} res - 응답 객체
 */
failureCostRouter.post('/', async (req: Request, res: Response) => {
    const { totalMonthlyUsers, trafficTrendDeviationPct, conversionRate } = req.body;

    // 🚨 필수 변수 검증 루틴 추가 (가드)
    if (!totalMonthlyUsers || !trafficTrendDeviationPct || !conversionRate) {
        return res.status(400).json({ error: "진단 지표 누락", message: "총 월간 사용자 수, 트래픽 변동률, 전환율 3가지 필수 지표를 모두 제공해야 합니다." });
    }

    try {
        // 핵심 서비스 로직 호출
        const result = await calculateFailureCost({
            totalMonthlyUsers: parseFloat(totalMonthlyUsers.toString()),
            trafficTrendDeviationPct: parseFloat(trafficTrendDeviationPct.toString()),
            conversionRate: parseFloat(conversionRate.toString())
        });

        // 성공적으로 계산된 결과를 반환합니다.
        return res.status(200).json({
            success: true,
            data: {
                failureCostAmount: result.cost, // 최종 Failure Cost 수치
                unit: "KRW",
                diagnostics: result.moduleDetails, // 근거 모듈 배열
                reportGeneratedAt: new Date().toISOString(),
            }
        });

    } catch (error) {
        console.error("Failure Cost API 처리 중 오류 발생:", error);
        return res.status(500).json({ success: false, message: "시스템 진단 과정에서 내부 오류가 발생했습니다." });
    }
});

export default failureCostRouter;