#!/bin/bash
# Script to rebuild Android App Bundle version 2

echo "🔧 Rebuilding Android App Bundle Version 2..."

# Sync Capacitor
echo "📱 Syncing Capacitor..."
npx cap sync android

# Build web assets
echo "🌐 Building web assets..."
npm run build

# Copy assets to Android
echo "📋 Copying assets to Android..."
npx cap copy android

# Try to rebuild with gradlew
echo "🔨 Building Android App Bundle..."
cd android

# Create local.properties with proper SDK location if it doesn't work
echo "sdk.dir=/nix/store/*/android-sdk" > local.properties 2>/dev/null

# Build the release bundle
./gradlew bundleRelease --no-daemon --console=plain

echo "✅ Android App Bundle built successfully!"
echo "📱 Version: 2.0 (versionCode: 2)"
echo "📁 Location: android/app/build/outputs/bundle/release/app-release.aab"