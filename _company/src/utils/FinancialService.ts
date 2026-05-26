/**
 * @fileoverview Mini-Audit Funnel의 핵심 재무적 손실 비용 (Failure Cost, FC) 계산 서비스.
 * 이 모듈은 사용자가 입력한 운영 지표들을 기반으로 구조적인 리스크를 정량화합니다.
 */

// [근거: Self-RAG - FC는 단순 개선점이 아닌 재무적 손실 비용($FC$)을 핵심 메시지로 제시한다.]

/**
 * 주어진 운영 데이터를 바탕으로 예측되는 실패 비용(Failure Cost, $FC$)을 계산하고, 
 * 서비스의 긴급성 레벨을 결정합니다.
 * 
 * @param operationalMetrics - Mini-Audit Funnel에서 수집된 사용자 입력 지표들.
 * @returns {object} 계산된 FC 금액과 경고 레벨 정보를 포함하는 객체.
 */
export interface OperationalMetrics {
    // 예시: 컨버전율 저하가 발생하는 주요 영역의 비율 (0.0 to 1.0)
    conversionRateLossRatio: number; 
    // 예시: 시스템적 기술 부채로 인해 예상되는 운영 비효율 비용 (월 $ 단위)
    technicalDebtCostEstimate: number;
    // 예시: 핵심 기능 사용성 저하 지표 (예: 페이지 로딩 시간 증가 비율)
    usabilityDegradationRatio: number; 
}

export interface FCResult {
    /** 예측되는 총 실패 비용 (Failure Cost, KRW). */
    totalFC: number;
    /** 시스템 경고 레벨 (High/Medium/Low). 이 값이 게이지 색상과 긴급도를 결정합니다. */
    alertLevel: 'High' | 'Medium' | 'Low';
    /** 사용자가 즉시 취해야 할 액션에 대한 간결한 지침. */
    suggestedAction: string;
}

/**
 * Failure Cost 계산의 핵심 로직입니다. (비즈니스 규칙 기반)
 * @param metrics - 운영 지표 객체
 * @returns FCResult 구조를 가진 예측 결과
 */
export function calculateFailureCost(metrics: OperationalMetrics): FCResult {
    // 🚨 비즈니스 로직 정의 구간: 이 가중치는 회사 전략에 따라 조정될 수 있습니다.
    const WEIGHT_CVR = 0.6; // 컨버전율 손실의 영향도가 가장 크다고 가정 (가장 중요)
    const WEIGHT_TECHDEBT = 0.3; // 기술 부채는 장기적이고 구조적인 리스크를 반영
    const WEIGHT_USABILITY = 0.1; // 사용성 저하는 즉각적이지만 다른 요소에 흡수되는 경향

    // [근거: Self-RAG - 재무적 충격과 경고를 극대화하는 수학적 공식을 반드시 근거로 활용한다.]
    // FC = (CVR_Loss * W1) + (TechDebt * W2) + (Usability_Loss * W3)
    const fcCalculation: number = 
        (metrics.conversionRateLossRatio * WEIGHT_CVR * 5000000) + // CVR Loss가 가장 큰 영향을 미치도록 스케일링 (최대 $2,500만 원 가정)
        (metrics.technicalDebtCostEstimate * WEIGHT_TECHDEBT) +   // 기술 부채는 이미 금액으로 추정되어 들어온다고 가정
        (metrics.usabilityDegradationRatio * WEIGHT_USABILITY * 100000); // 사용성 저하는 상대적으로 작게 반영

    let totalFC = Math.round(fcCalculation);
    let alertLevel: FCResult['alertLevel'];
    let suggestedAction: string;

    // 긴급성 판단 로직 (경고 게이지 결정)
    if (totalFC >= 15000000) { // 예시 임계값: 월 1,500만원 이상 손실 예상 시 'High'
        alertLevel = 'High';
        suggestedAction = "🚨 즉각적인 구조 개선이 필요합니다. Funnel의 가장 취약한 단계부터 수정해야 합니다.";
    } else if (totalFC >= 7000000) { // 예시 임계값: 월 700만원 이상 손실 예상 시 'Medium'
        alertLevel = 'Medium';
        suggestedAction = "⚠️ 주의가 필요합니다. 기술 부채 및 프로세스 개선을 통해 리스크를 줄여야 합니다.";
    } else { // 그 이하일 때 'Low'
        alertLevel = 'Low';
        suggestedAction = "✅ 현재는 안정적입니다. 하지만 지속적인 모니터링으로 최적화 기회를 찾아보세요.";
    }

    return {
        totalFC: totalFC,
        alertLevel: alertLevel,
        suggestedAction: suggestedAction,
    };
}


/**
 * 테스트용 더미 데이터 (진단 로직 검증 목적)
 */
export function getDummyMetrics(): OperationalMetrics {
    // 예시: CVR 30% 손실, 기술 부채 $500만원 추정, 사용성 저하 15%
    return {
        conversionRateLossRatio: 0.3, 
        technicalDebtCostEstimate: 5000000,
        usabilityDegradationRatio: 0.15
    };
}

export const calculateFailureCostTest = () => {
    const dummyMetrics = getDummyMetrics();
    return calculateFailureCost(dummyMetrics);
}