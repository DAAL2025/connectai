-- 테이블 이름: growth_engine_retainer
-- 목적: 고객별 성장 엔진 계약, KPI 추적 및 워크플로우 관리
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    subscription_tier VARCHAR(50) NOT NULL CHECK (subscription_tier IN ('$50', '$250', '$500')) NOT NULL,
    status VARCHAR(50) DEFAULT 'Active', -- Active, Trial, Paused, Cancelled
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE growth_metrics (
    metric_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    -- 핵심 KPI 정의: 예측 정확도, 자동화 성공률 등
    kpi_prediction_accuracy NUMERIC(5, 2) NOT NULL, -- 예: 0.85 (85%)
    automation_success_rate NUMERIC(5, 2) NOT NULL, -- 예: 0.98 (98%)
    engagement_score INTEGER NOT NULL, -- 사용자 참여도 점수
    -- 타임스탬프 기반 기록
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE workflow_steps (
    step_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    step_name VARCHAR(255) NOT NULL, -- 예: 'Data Ingestion Setup', 'Prediction Model Training'
    status VARCHAR(50) DEFAULT 'Pending', -- Pending, In Progress, Completed, Failed
    start_date TIMESTAMP WITH TIME ZONE,
    end_date TIMESTAMP WITH TIME ZONE,
    details TEXT, -- 상세 로그 및 설명 (Designer/Business의 명세서 반영)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 타임스탬프 기반으로 데이터 접근 최적화
CREATE INDEX idx_metrics_customer_id ON growth_metrics(customer_id);
CREATE INDEX idx_workflow_customer_id ON workflow_steps(customer_id);