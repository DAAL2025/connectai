// ============================================================================
// [File: src/api/schemas/FailureCostSchema.ts]
// API Contract Definition for Failure Cost Simulation Module (v1.0)
// Purpose: To calculate and display the 'Systemic Failure Cost' by breaking down 
// the loss into measurable, structural defects.
// ============================================================================

/**
 * @typedef {Object} InputVariables
 * @description 사용자에게서 입력받을 원본 운영 데이터를 정의합니다. (POST Request Body)
 */
export interface InputVariables {
    /** 고객의 핵심 가치 제안(Value Proposition)과 관련된 산업군 (예: SaaS_B2B, Retail_ECommerce, EduTech). [근거: Researcher] */
    industrySector: 'SaaS_B2B' | 'Retail_ECommerce' | 'EduTech' | string;

    /** 시스템의 규모를 나타내는 총 예상 사용자 수 (Active Users). */
    totalMonthlyUsers: number; 
    
    /** 현재 평균 트래픽(방문자) 추이. (예: 지난 3개월 대비 하락률 %) */
    trafficTrendDeviationPct: number; 

    /** 운영 인력의 규모 및 효율성 지표. (예: PMO/마케팅 인원 수, 또는 특정 기능 담당 인원 수) */
    operationalStaffCount: number;

    /** 현재 시스템에서 가장 의심되는 병목 구간 또는 리스크 지점. (예: 결제 퍼널 이탈률 높음, 데이터 연동 실패 등). [근거: Writer] */
    suspectedBottleneckArea: string; 
}


/**
 * @typedef {Object} CostBreakdownItem
 * @description Failure Cost를 구성하는 하나의 세부 손실 요소를 정의합니다. (단계별 설명 제공 목적)
 * @param name - 손실 요소의 명칭 (예: '결제 퍼널 이탈 비용', '운영 비효율성').
 * @param cause - 왜 문제가 발생했는지에 대한 구조적 원인(Pain Point). [근거: Self-RAG, Writer]
 * @param metricImpact - 이 문제로 인해 영향을 받은 구체적인 지표. (예: LTV 15% 감소).
 * @param lossValue - 해당 요소에서 계산된 재정적 손실액.
 */
export interface CostBreakdownItem {
    name: string;
    cause: string;
    metricImpact: string;
    lossValue: number; // 금액 단위 (단위 통화 사용 가정)
}


/**
 * @typedef {Object} FailureCostReport
 * @description API 호출의 최종 결과 구조체입니다. (POST Response Body)
 */
export interface FailureCostReport {
    // --- 1. 메타 정보 및 요약 ---
    simulationId: string; // 고유 시뮬레이션 ID
    inputVariablesUsed: InputVariables; // 어떤 변수를 가지고 계산했는지 기록 (재현성 확보)

    /** 핵심 가치 제안을 반영하여, 이 비용이 '잠재적 수익'임을 강조합니다. */
    totalFailureCost: number; 
    
    /** Failure Cost를 줄이기 위해 필수적인 최소 투자 금액 또는 개선 목표액. */
    estimatedMitigationInvestment: number;

    // --- 2. 단계별 상세 분석 (Authority Building) ---
    /** 
     * 실패 비용을 구성하는 개별 항목들의 배열입니다. 이 구조가 UI의 '단계적 진단' 섹션에 활용됩니다. 
     * 총합이 totalFailureCost를 만듭니다. [근거: Self-RAG, Writer]
     */
    breakdownItems: CostBreakdownItem[];

    // --- 3. 권고 및 다음 액션 유도 (CTA Integration) ---
    /** 실패 비용을 줄이기 위한 가장 시급한 Top 3 개선 영역입니다. */
    priorityActionAreas: string[]; // 예: ['재정적 리스크 진단', 'Growth OS 재설계', 'API 연동 안정화']

    // --- 4. 계산 메커니즘 설명 (Transparency) ---
    /** 각 CostBreakdownItem이 어떤 공식을 통해 산출되었는지 간략하게 명시하여 신뢰도를 높입니다. */
    calculationLogicNotes: {
        item: string; // 어느 항목에 대한 로직인지
        formulaDescription: string; // "Lost Revenue = (Traffic * Conversion Rate) - Current Performance" 등
    }[];
}

// ----------------------------------------------------------------------------
// API Endpoints Definition Example (FastAPI/Express Style)
// POST /api/v1/failure-cost/simulate
/**
 * @param body {InputVariables} userInputs - 사용자로부터 받아온 입력 변수들.
 * @returns {FailureCostReport} 계산된 시스템적 실패 비용 보고서 객체.
 */
export type FailureCostSimulationAPI = (userInputs: InputVariables) => Promise<FailureCostReport>;