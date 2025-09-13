# My Branches - Build & Deployment Guide

## Overview
This guide provides step-by-step instructions for building and deploying My Branches to both Apple App Store and Google Play Store, including certificate setup, signing configuration, and distribution preparation.

## Prerequisites

### Development Environment Setup
- **Node.js**: 18+ installed
- **npm**: Latest version
- **Capacitor CLI**: `npm install -g @capacitor/cli`
- **Xcode**: 15+ (for iOS builds) - macOS required
- **Android Studio**: Latest version with Android SDK
- **Git**: For version control

### Apple Developer Requirements
- **Apple Developer Account**: $99/year subscription
- **macOS Computer**: Required for iOS builds
- **Xcode Command Line Tools**: `xcode-select --install`

### Google Play Developer Requirements
- **Google Play Developer Account**: $25 one-time registration fee
- **Java Development Kit (JDK)**: 11+ required

## Project Setup & Dependencies

### 1. Install Dependencies
```bash
# Install project dependencies
npm install

# Install Capacitor CLI globally (if not already installed)
npm install -g @capacitor/cli

# Verify Capacitor installation
npx cap --version
```

### 2. Environment Configuration
Create production environment variables:

```bash
# Create production environment file
touch .env.production

# Add production configuration
cat << EOF > .env.production
NODE_ENV=production
DATABASE_URL=your_production_database_url
REPLIT_AUTH_CLIENT_ID=your_production_client_id
REPLIT_AUTH_CLIENT_SECRET=your_production_client_secret
STRIPE_SECRET_KEY=your_production_stripe_key
REVENUECAT_API_KEY=your_production_revenuecat_key
FIREBASE_SERVICE_ACCOUNT_KEY=your_production_firebase_key
APP_URL=https://mybranches.app
EOF
```

### 3. Build Web Assets
```bash
# Build optimized production assets
npm run build

# Verify build output
ls -la dist/public/
```

## iOS App Store Build Process

### Step 1: Apple Developer Account Setup

#### 1.1 Create App Store Connect App
1. **Sign in to App Store Connect**: https://appstoreconnect.apple.com
2. **Create New App**:
   - Platform: iOS
   - Name: "My Branches - Family Collaboration"
   - Primary Language: English
   - Bundle ID: `com.mybranches.app`
   - SKU: `mybranches-family-app`

#### 1.2 Configure App Information
```
Basic Information:
- Privacy Policy URL: https://mybranches.app/privacy
- App Category: Primary (Lifestyle), Secondary (Productivity)
- Content Rights: No, this app does not use third-party content

Pricing and Availability:
- Price: Free (with in-app purchases)
- Availability: All countries
- App Store Distribution: Yes

Version Information:
- Version: 1.0.0
- Copyright: 2025 My Branches
- Trade Representative Contact: [Your contact info]
- App Review Contact: [Your contact info]
- Marketing URL: https://mybranches.app
- Support URL: https://mybranches.app/support
```

### Step 2: iOS Certificate & Provisioning Setup

#### 2.1 Create iOS Distribution Certificate
```bash
# Generate Certificate Signing Request (CSR)
# Open Keychain Access > Certificate Assistant > Request a Certificate from a Certificate Authority
# Save CSR file as: MyBranches_CSR.certSigningRequest
```

1. **Apple Developer Portal**: https://developer.apple.com/account/
2. **Certificates, Identifiers & Profiles** → **Certificates** → **+**
3. **Select**: iOS Distribution (App Store and Ad Hoc)
4. **Upload**: CSR file created above
5. **Download**: Distribution certificate
6. **Install**: Double-click to install in Keychain

#### 2.2 Create App ID
1. **Identifiers** → **App IDs** → **+**
2. **Configuration**:
   - Platform: iOS, tvOS, watchOS
   - Description: "My Branches Family Collaboration"
   - Bundle ID: Explicit (`com.mybranches.app`)
   - Capabilities: 
     - Associated Domains (for universal links)
     - Push Notifications
     - In-App Purchase

#### 2.3 Create Distribution Provisioning Profile
1. **Profiles** → **Distribution** → **+**
2. **Select**: App Store
3. **App ID**: Select `com.mybranches.app`
4. **Certificate**: Select distribution certificate created above
5. **Profile Name**: "My Branches App Store Distribution"
6. **Download and Install**: Double-click to install

### Step 3: Xcode Project Configuration

#### 3.1 Open and Configure Xcode Project
```bash
# Sync Capacitor project
npx cap sync ios

# Open Xcode workspace
npx cap open ios
```

#### 3.2 Xcode Project Settings
1. **Project Navigator** → Select **App** project
2. **TARGETS** → **App** → **General**:
   ```
   Display Name: My Branches
   Bundle Identifier: com.mybranches.app
   Version: 1.0.0
   Build: 1
   
   Deployment Info:
   - iOS Deployment Target: 13.0
   - Device Orientation: Portrait, Landscape Left, Landscape Right
   
   App Icons and Launch Screen:
   - App Icons Source: AppIcon (should be configured)
   - Launch Screen File: LaunchScreen
   ```

3. **Signing & Capabilities**:
   ```
   Team: [Your Apple Developer Team]
   Provisioning Profile: My Branches App Store Distribution
   Bundle Identifier: com.mybranches.app
   
   Capabilities:
   ✅ Associated Domains: applinks:mybranches.app
   ✅ Push Notifications
   ✅ In-App Purchase
   ```

4. **Build Settings**:
   ```
   Code Signing Identity (Release): iOS Distribution
   Provisioning Profile (Release): My Branches App Store Distribution
   ```

### Step 4: Build and Archive for App Store

#### 4.1 Archive Build
```bash
# Clean build folder
# In Xcode: Product → Clean Build Folder

# Build for Archive
# In Xcode: Product → Archive
```

#### 4.2 Upload to App Store Connect
1. **Xcode Organizer** opens after successful archive
2. **Select Archive** → **Distribute App**
3. **Select**: App Store Connect
4. **Select**: Upload
5. **App Store Connect Distribution Options**:
   - Include bitcode: No (deprecated)
   - Upload your app's symbols: Yes
   - Manage Version and Build Number: Yes
6. **Re-sign**: Automatically manage signing
7. **Review Summary** → **Upload**

#### 4.3 Process in App Store Connect
1. **Build Processing**: Wait 10-30 minutes for processing
2. **Build Available**: Receive email when ready
3. **Configure Release**: 
   - App Store Connect → My Apps → My Branches
   - iOS App → App Store → Prepare for Submission
   - Build → Select uploaded build

## Android Google Play Store Build Process

### Step 1: Google Play Console Setup

#### 1.1 Create Google Play Console App
1. **Sign in to Google Play Console**: https://play.google.com/console
2. **Create App**:
   - App name: "My Branches - Family Collaboration"
   - Default language: English (United States)
   - App or game: App
   - Free or paid: Free (with in-app purchases)

#### 1.2 Configure App Information
```bash
# Complete App Content questionnaire:
Privacy Policy: https://mybranches.app/privacy
App access: All functionality available without restrictions
Content rating: 4+ (Everyone)
Target audience: 13 and over
App category: Lifestyle
Store presence: Available on Google Play
```

### Step 2: Android Keystore Creation & Signing

#### 2.1 Generate Release Keystore
```bash
# Create keystore directory
mkdir -p android/keystores

# Generate release keystore
keytool -genkey -v -keystore android/keystores/my-branches-release.keystore \
  -alias my-branches-key \
  -keyalg RSA \
  -keysize 2048 \
  -validity 25000

# You'll be prompted for:
# - Keystore password: [Create strong password]
# - Key password: [Create strong password]
# - Personal information: [Your/company information]

# IMPORTANT: Store passwords securely - you'll need them for all future releases
```

#### 2.2 Configure Gradle Signing
Create signing configuration file:

```bash
# Create gradle.properties in android directory
cat << EOF > android/gradle.properties
MYAPP_RELEASE_STORE_FILE=keystores/my-branches-release.keystore
MYAPP_RELEASE_KEY_ALIAS=my-branches-key
MYAPP_RELEASE_STORE_PASSWORD=your_keystore_password
MYAPP_RELEASE_KEY_PASSWORD=your_key_password
EOF

# Add gradle.properties to .gitignore to keep credentials secure
echo "android/gradle.properties" >> .gitignore
```

#### 2.3 Update build.gradle Signing Configuration
Edit `android/app/build.gradle`:

```gradle
android {
    // ... existing configuration

    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
                storePassword MYAPP_RELEASE_STORE_PASSWORD
                keyAlias MYAPP_RELEASE_KEY_ALIAS
                keyPassword MYAPP_RELEASE_KEY_PASSWORD
            }
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

### Step 3: Build Android Release

#### 3.1 Sync Capacitor and Build
```bash
# Sync Capacitor project
npx cap sync android

# Navigate to Android directory
cd android

# Clean previous builds
./gradlew clean

# Build release APK
./gradlew assembleRelease

# Or build App Bundle (recommended for Play Store)
./gradlew bundleRelease

# Output locations:
# APK: android/app/build/outputs/apk/release/app-release.apk
# AAB: android/app/build/outputs/bundle/release/app-release.aab
```

#### 3.2 Verify Release Build
```bash
# Verify APK signature
jarsigner -verify -verbose -certs android/app/build/outputs/apk/release/app-release.apk

# Check APK contents
aapt dump badging android/app/build/outputs/apk/release/app-release.apk

# Test install on device
adb install android/app/build/outputs/apk/release/app-release.apk
```

### Step 4: Upload to Google Play Console

#### 4.1 Upload App Bundle
1. **Google Play Console** → **My Branches** → **Release** → **Production**
2. **Create New Release**
3. **App bundles and APKs** → **Upload** → Select AAB file
4. **Release name**: "1.0.0 - Initial Release"
5. **Release notes**:
   ```
   🎉 Welcome to My Branches!
   
   ✨ What's New:
   • Family collaboration platform launch
   • Real-time family group chat
   • Event planning and coordination
   • Task management for families
   • Secure family photo sharing
   • Premium mailing label printing
   
   Perfect for keeping your family connected and organized!
   ```

## Version Management

### iOS Version Updates
```bash
# Update version in Xcode:
# 1. Select App target → General
# 2. Update Version (marketing version): 1.0.1
# 3. Update Build number: 2
# 4. Archive and upload new build
```

### Android Version Updates
```gradle
// Update android/app/build.gradle:
defaultConfig {
    versionCode 2          // Increment for each release
    versionName "1.0.1"    // Marketing version
}
```

### Package.json Version Sync
```bash
# Keep package.json version in sync
npm version patch   # 1.0.0 → 1.0.1
npm version minor   # 1.0.1 → 1.1.0
npm version major   # 1.1.0 → 2.0.0
```

## Testing Production Builds

### iOS Testing
```bash
# TestFlight Beta Testing
# 1. Upload build to App Store Connect
# 2. Add internal testers in TestFlight
# 3. Send beta invitations
# 4. Collect feedback before public release
```

### Android Testing
```bash
# Internal Testing Track
# 1. Upload AAB to internal testing track
# 2. Add tester email addresses
# 3. Share testing link
# 4. Collect feedback and crash reports
```

## Deployment Checklist

### Pre-Submission Checklist
- [ ] Production environment variables configured
- [ ] App builds successfully on both platforms
- [ ] All features tested in release builds
- [ ] App store assets uploaded (screenshots, descriptions)
- [ ] Legal documents accessible via URLs
- [ ] Version numbers updated consistently
- [ ] Certificates and signing working correctly

### iOS Submission Checklist
- [ ] App Store Connect app created and configured
- [ ] iOS Distribution certificate installed
- [ ] App ID created with required capabilities
- [ ] Distribution provisioning profile installed
- [ ] Xcode project properly configured and signed
- [ ] Archive uploaded to App Store Connect
- [ ] App information, screenshots, and metadata complete
- [ ] Submit for App Store review

### Android Submission Checklist
- [ ] Google Play Console app created
- [ ] Release keystore generated and secured
- [ ] Gradle signing configuration complete
- [ ] App bundle (.aab) built and tested
- [ ] Content rating questionnaire completed
- [ ] Store listing complete with descriptions and graphics
- [ ] Upload to production track and submit for review

## Troubleshooting Common Issues

### iOS Issues
```bash
# Code signing issues
# 1. Check certificate validity in Keychain
# 2. Verify provisioning profile matches bundle ID
# 3. Ensure correct team selected in Xcode

# Build failures
# 1. Clean build folder: Product → Clean Build Folder
# 2. Delete derived data: ~/Library/Developer/Xcode/DerivedData
# 3. Re-sync Capacitor: npx cap sync ios
```

### Android Issues
```bash
# Gradle build issues
./gradlew clean
rm -rf android/.gradle
rm -rf android/app/build

# Signing issues
# 1. Verify keystore passwords in gradle.properties
# 2. Check keystore file path
# 3. Ensure signing config matches build type

# Capacitor sync issues
npx cap clean android
npx cap sync android
```

### General Issues
```bash
# Dependency issues
rm -rf node_modules package-lock.json
npm install

# Capacitor issues
npx cap doctor
npx cap sync
```

## Security Best Practices

### Credential Management
- **Never commit**: Keystore files, certificates, or passwords to version control
- **Use environment variables**: For sensitive configuration
- **Secure storage**: Store credentials in secure password managers
- **Team access**: Limit certificate access to authorized team members

### Build Security
- **Verify signatures**: Always verify signed builds before distribution
- **Secure build environment**: Use clean, secure machines for release builds
- **Audit dependencies**: Regularly audit npm and native dependencies
- **Monitor releases**: Set up monitoring for production app performance

---

**This comprehensive build and deployment guide ensures My Branches can be successfully built, signed, and submitted to both app stores with proper security and version management practices.**