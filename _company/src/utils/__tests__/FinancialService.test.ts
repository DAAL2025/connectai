import { calculateFailureCost, getDummyMetrics } from '../FinancialService';
import { describe, it, expect } from 'vitest'; // 가정: Vitest 사용

describe('calculateFailureCost', () => {
    it('Should correctly calculate FC based on High risk scenario (High loss)', () => {
        // [근거: Self-RAG - 재무적 충격과 경고를 극대화하는 수학적 공식을 반드시 근거로 활용한다.]
        const metrics = { 
            conversionRateLossRatio: 0.5, // 높은 손실률 가정
            technicalDebtCostEstimate: 10000000, // 기술 부채도 높다고 가정
            usabilityDegradationRatio: 0.3 
        };
        const result = calculateFailureCost(metrics);

        expect(result.alertLevel).toBe('High');
        // 계산 검증 (대략적인 값으로만 체크하고, 실제 구현 시 정확한 수식 유도 필요)
        expect(result.totalFC).toBeGreaterThanOrEqual(15000000); 
    });

    it('Should correctly calculate FC based on Medium risk scenario', () => {
        const metrics = { 
            conversionRateLossRatio: 0.2, 
            technicalDebtCostEstimate: 3000000, 
            usabilityDegradationRatio: 0.15 
        };
        const result = calculateFailureCost(metrics);

        expect(result.alertLevel).toBe('Medium');
        expect(result.totalFC).toBeGreaterThanOrEqual(7000000) && expect(result.totalFC) < 15000000;
    });

    it('Should correctly calculate FC based on Low risk scenario', () => {
        const metrics = { 
            conversionRateLossRatio: 0.05, // 낮은 손실률 가정
            technicalDebtCostEstimate: 500000, 
            usabilityDegradationRatio: 0.05 
        };
        const result = calculateFailureCost(metrics);

        expect(result.alertLevel).toBe('Low');
        expect(result.totalFC).toBeLessThan(7000000);
    });
});