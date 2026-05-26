import React, { useState, useEffect } from 'react';

interface ErrorData {
  status: number; // HTTP Status Code (4xx or 5xx)
  message: string; // The specific error message
  title: string; // Title for the error state
  reason: string; // Detailed reason/cause
  actionSteps: string[]; // Actionable steps for the user
}

interface ErrorStateComponentProps {
  errorData: ErrorData | null;
  onActionClick: (action: string) => void; // Function to trigger an action step
  isLoading: boolean;
}

const ErrorStateComponent: React.FC<ErrorStateComponentProps> = ({ errorData, onActionClick, isLoading }) => {
  if (!errorData) return null;

  // 1. Determine visual style based on status (Simulating the design spec colors)
  const statusColor = errorData.status >= 500 ? 'bg-red-600 border-red-800' : 'bg-yellow-500 border-yellow-700';

  return (
    <div className={`p-6 rounded-lg shadow-xl transition-all duration-300 ${statusColor}`}>
      <h2 className="text-3xl font-bold mb-4 flex items-center">
        <span className="mr-3 text-4xl">{errorData.status}</span>
        {errorData.title}
      </h2>

      {/* Problem Cause (Why) */}
      <div className="mb-6 border-b pb-4">
        <h3 className="text-xl font-semibold text-gray-800 mb-2">문제의 원인 (Why)</h3>
        <p className="text-gray-600">{errorData.reason}</p>
      </div>

      {/* Visual Data/Metrics (Simulating the integration point) */}
      {/* Placeholder for dynamic data visualization based on LAI context */}
      <div className="mb-6">
        <h3 className="text-xl font-semibold text-gray-800 mb-2">재무적 영향 예상치</h3>
        <p className="text-lg font-bold text-orange-600">잠재적 손실: {errorData.status >= 500 ? '높음' : '중간'}</p>
      </div>

      {/* Action Steps (Action Step) - Most Important */}
      <div className="mt-8 pt-4 border-t">
        <h3 className="text-xl font-semibold text-gray-800 mb-3">다음 단계 (Action Step)</h3>
        <ul className="space-y-3">
          {errorData.actionSteps.map((step, index) => (
            <li key={index} className="flex items-start">
              <span className="text-xl mr-3 text-green-500 font-bold">{index + 1}.</span>
              <p className="text-gray-700">{step}</p>
            </li>
          ))}
        </ul>
        {/* CTA: Triggering the workflow */}
        <button
          onClick={() => onActionClick(errorData.actionSteps[0])}
          disabled={isLoading}
          className={`mt-5 w-full py-3 px-4 rounded-lg font-semibold transition duration-200 ${isLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-md'}`}
        >
          {isLoading ? '처리 중...' : `${errorData.actionSteps[0]} 시작하기`}
        </button>
      </div>
    </div>
  );
};

export default ErrorStateComponent;