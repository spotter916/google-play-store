# My Branches - Family Collaboration App

A comprehensive family collaboration platform with household-level premium subscriptions, profile management, group collaboration, event planning, real-time chat, and cross-platform mobile apps.

## Features

- **Family Households**: Create and join family groups
- **Event Planning**: Organize family events and activities  
- **Real-time Chat**: Stay connected with instant messaging
- **Photo Sharing**: Share family memories
- **Task Management**: Coordinate family tasks
- **Premium Subscriptions**: $5.99/month or $60/year for advanced features
- **Push Notifications**: Stay updated on important family activities

## Tech Stack

- **Frontend**: React + TypeScript + Vite
- **Backend**: Node.js + Express + PostgreSQL
- **Mobile**: Capacitor (iOS & Android)
- **Real-time**: WebSocket for chat
- **Payments**: RevenueCat for subscriptions
- **Authentication**: Replit Auth

## Mobile Apps

- **Android**: Available on Google Play Store
- **iOS**: Built with Xcode Cloud for App Store

## Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
npx cap sync
```

### iOS

```bash
cd ios/App
# Open App.xcworkspace in Xcode for local builds
# Or use Xcode Cloud for automatic builds
```

### Android

```bash
cd android
./gradlew bundleRelease
```

## App Store Information

- **Bundle ID**: com.mybranches.app
- **Version**: 1.0
- **Category**: Social Networking / Productivity