import { FailureCostReport, InputVariables } from '../api/schemas/FailureCostSchema';

/**
 * @private 
 * Failure Cost 계산의 핵심 비즈니스 로직입니다.
 * 이 함수는 API 요청을 받아 단계별로 비용을 추정하고 보고서를 생성합니다.
 * @param userInputs - 사용자가 입력한 운영 데이터 변수들.
 * @returns FailureCostReport 객체
 */
export function calculateFailureCost(userInputs: InputVariables): Promise<FailureCostReport> {
    // [TODO]: 실제 환경에서는 복잡한 비즈니스 로직과 통계 모델이 들어갑니다. 
    // 현재는 예시적인 구조만 구현합니다.

    const totalLoss = calculateTotalSimulatedLoss(userInputs);

    const report = {
        simulationId: `FCC-${Date.now()}-${Math.random().toString(36).substring(2, 8)}`,
        inputVariablesUsed: userInputs,
        totalFailureCost: Math.round(totalLoss * 100) / 100, // 소수점 둘째 자리까지 반올림
        estimatedMitigationInvestment: totalLoss * 0.3, // 임시 가이드라인: 손실의 30%를 투자해야 함
        breakdownItems: [
            {
                name: '결제 퍼널 이탈 비용 (Funnel Leakage)',
                cause: `[${userInputs.suspectedBottleneckArea}]: ${userInputs.industrySector} 산업에서 필수적인 결제 단계를 우회하는 사용자가 발생함.`,
                metricImpact: `최근 3개월 대비 전환율 -15% 하락 예상.`;
                lossValue: totalLoss * 0.4; // 예시 비율
            },
            {
                name: '운영 자동화 결여 비용 (Operational Debt)',
                cause: `${userInputs.operationalStaffCount}명의 인력이 수동으로 처리해야 하는 반복 작업을 시스템이 대체하지 못함.`,
                metricImpact: `월평균 120시간의 노동력 손실 발생 예상.`;
                lossValue: totalLoss * 0.35; // 예시 비율
            },
            {
                name: '시장 기회 상실 비용 (Opportunity Cost)',
                cause: `트래픽 감소(${Math.abs(userInputs.trafficTrendDeviationPct)}%)에 대응하는 선제적 마케팅 및 시스템 개선이 이루어지지 않음.`;
                metricImpact: `잠재 시장 성장률 대비 실제 매출 달성 실패율 증대.` ;
                lossValue: totalLoss * 0.25; // 예시 비율
            }
        ],
        priorityActionAreas: ['시스템 감사 (System Audit)', 'Growth OS 재설계', '핵심 퍼널 최적화'],
        calculationLogicNotes: [
            { item: '결제 퍼널 이탈 비용', formulaDescription: `(총 예상 매출) * (이탈률 증가분) * (산업 가중치 ${userInputs.industrySector})` },
            { item: '운영 자동화 결여 비용', formulaDescription: `(인력 수 × 평균 시간당 기회비용) * 운영 기간` }
        ]
    };

    return Promise.resolve(report);
}


/** @private */
function calculateTotalSimulatedLoss(inputs: InputVariables): number {
    // 이 함수가 전체 로직을 총합하여 Failure Cost를 계산합니다.
    const baseCost = 100000; // 기본값 설정

    let costFactor = 1.0;

    if (inputs.industrySector === 'SaaS_B2B') {
        costFactor *= 1.5; // B2B는 평균적으로 고가치 거래를 함
    } else if (inputs.industrySector === 'Retail_ECommerce') {
        costFactor *= 1.2;
    }

    // 트래픽 감소율이 클수록 비용 증가
    if (Math.abs(inputs.trafficTrendDeviationPct) > 10) {
        costFactor *= (1 + Math.abs(inputs.trafficTrendDeviationPct) / 50);
    }

    return baseCost * costFactor;
}