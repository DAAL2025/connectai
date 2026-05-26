// /volumes/daal/documents/01.work/connect ai/_company/pages/api/v1/audit.ts

import { NextApiRequest, NextApiResponse } from 'next';
import { calculateLossCost, determineWarningLevel } from '@/utils/FinancialService'; // 경로 조정 필요

// [근거: Self-RAG] API 게이트웨이 역할 수행을 위해 서비스 로직 분리 필수.
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  // 1. 입력 유효성 검증 (Input Validation - Defensive Coding)
  const { featureA, featureB, userInteractionScore } = req.body;

  if (typeof featureA !== 'number' || typeof featureB !== 'number' || typeof userInteractionScore !== 'number') {
    return res.status(400).json({ error: "Invalid input data type. All fields must be numbers." });
  }

  try {
    // 2. 핵심 비즈니스 로직 호출 (Service Layer Call)
    // FinancialService.ts의 calculateLossCost를 통해 FC 계산 수행
    const fcAmount = calculateLossCost(featureA, featureB, userInteractionScore);

    // 3. 경고 레벨 및 메시지 결정
    const { warningLevel, message } = determineWarningLevel(fcAmount);

    // 4. 최종 결과 반환 (Consistency Check)
    const result = {
      fcAmount: parseFloat(fcAmount.toFixed(2)), // 금액은 소수점 둘째 자리로 고정
      warningLevel: warningLevel,
      message: message,
    };

    return res.status(200).json(result);

  } catch (error) {
    console.error("Audit API Error:", error);
    // 5. 에러 응답 처리
    return res.status(500).json({ error: 'Failed to process audit data due to a structural issue.' });
  }
}