#!/bin/bash
# Next.js 프로젝트 초기 설정 스크립트
set -e

echo "Setting up Next.js project..."
npx create-next-app@latest daal-profit-lab --ts --eslint --tailwind --app --src-dir --use-npm

cd daal-profit-lab

echo "Installing necessary dependencies (Prisma, PayPal SDK placeholder)..."
npm install prisma typescript ts-node @types/node --save-dev
npm install @prisma/client paypal-sdk # 실제 PayPal SDK는 추후 API 연동 시 설치할 예정

echo "Initializing Prisma..."
npx prisma init --datasource-provider postgresql

echo "Setup complete. Please review the generated files and set up environment variables."