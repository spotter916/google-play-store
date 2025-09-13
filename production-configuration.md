# My Branches - Production Configuration Guide

**Version: 1.0.0**
**Target Platforms: iOS App Store, Google Play Store**

## 1. App Store Configuration Overview

### Current App Identifiers
- **Bundle ID**: `com.mybranches.app`
- **App Name**: `My Branches`
- **Display Name**: `My Branches - Family Collaboration`
- **Version**: `1.0.0` (initial release)
- **Build Number**: `1` (will increment for each submission)

### Supported Platforms
- **iOS**: 13.0+ (recommended for modern family-friendly features)
- **Android**: API 24+ (Android 7.0) for broad device compatibility

## 2. Capacitor Configuration Review

### Current Configuration Status ✅
The `capacitor.config.ts` is properly configured with:

```typescript
const config: CapacitorConfig = {
  appId: 'com.mybranches.app',
  appName: 'My Branches',
  webDir: 'dist/public',
  // Production-ready server configuration
  server: {
    androidScheme: 'https',
    // Development server URL is conditionally applied
    url: process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : undefined,
    cleartext: process.env.NODE_ENV === 'development',
  }
};
```

### Key Production Features
- **Deep Linking**: Properly configured for `mybranches://` scheme
- **Universal Links**: Set up for iOS and Android
- **Splash Screen**: Professional branding with 2-second display
- **Status Bar**: Consistent purple theme (#7c3aed)

## 3. iOS Configuration (App Store)

### Info.plist Configuration ✅
Located: `ios/App/App/Info.plist`

**Key Settings:**
- Bundle Display Name: "My Branches"
- Bundle Identifier: Uses Xcode project variable
- Version String: Uses marketing version from Xcode
- URL Schemes: `mybranches` for deep linking
- Associated Domains: `applinks:mybranches.app`

### Required iOS Updates for Production

#### 3.1 Update Xcode Project Settings
```bash
# Open Xcode project
open ios/App/App.xcworkspace
```

**Configure in Xcode:**
1. **General Tab:**
   - Display Name: "My Branches"
   - Bundle Identifier: com.mybranches.app
   - Version: 1.0.0
   - Build: 1

2. **Signing & Capabilities:**
   - Team: [Your Apple Developer Team]
   - Automatically manage signing: ✅
   - Bundle Identifier: com.mybranches.app

3. **Associated Domains:**
   - Add: `applinks:mybranches.app`

#### 3.2 Privacy Usage Descriptions
Add to Info.plist if using device features:
```xml
<!-- For photo library access -->
<key>NSPhotoLibraryUsageDescription</key>
<string>My Branches needs access to your photo library to share family photos within your groups.</string>

<!-- For camera access -->
<key>NSCameraUsageDescription</key>
<string>My Branches needs camera access to take family photos to share with your groups.</string>

<!-- For push notifications -->
<key>NSUserNotificationsUsageDescription</key>
<string>My Branches sends notifications for family events, messages, and important updates.</string>
```

## 4. Android Configuration (Google Play Store)

### AndroidManifest.xml Configuration ✅
Located: `android/app/src/main/AndroidManifest.xml`

**Key Settings:**
- Package Name: `com.mybranches.app`
- App Name: Defined in strings.xml
- Deep Links: Properly configured for `mybranches://` and HTTPS links

### Required Android Updates for Production

#### 4.1 Update build.gradle Versions
File: `android/app/build.gradle`

**Current Settings (Good for Initial Release):**
```gradle
defaultConfig {
    applicationId "com.mybranches.app"
    versionCode 1
    versionName "1.0"
}
```

#### 4.2 Production Build Configuration
```gradle
buildTypes {
    release {
        minifyEnabled true  // Enable for production
        shrinkResources true  // Reduce APK size
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        
        // Production-specific configurations
        debuggable false
        jniDebuggable false
        renderscriptDebuggable false
    }
}
```

#### 4.3 App Signing Configuration
Add signing config for release builds:
```gradle
android {
    signingConfigs {
        release {
            storeFile file("../my-branches-keystore.jks")
            storePassword System.getenv("STORE_PASSWORD")
            keyAlias System.getenv("KEY_ALIAS")
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            // ... other release settings
        }
    }
}
```

## 5. Version Management Strategy

### Semantic Versioning
Follow semantic versioning (MAJOR.MINOR.PATCH):
- **1.0.0**: Initial App Store release
- **1.0.1**: Bug fixes and minor improvements
- **1.1.0**: New features (e.g., enhanced premium features)
- **2.0.0**: Major updates (e.g., UI redesign)

### Build Number Management
- **iOS**: Increment build number for each App Store submission
- **Android**: Increment versionCode for each Play Store submission

### Version Update Checklist
When updating versions:
1. Update `package.json` version
2. Update iOS project version in Xcode
3. Update Android `versionCode` and `versionName`
4. Update `capacitor.config.ts` if needed
5. Tag release in version control

## 6. Environment Configuration

### Production Environment Variables
Required for production builds:

```bash
# Server Configuration
NODE_ENV=production
DATABASE_URL=[Production database URL]

# Authentication
REPLIT_AUTH_CLIENT_ID=[Production client ID]
REPLIT_AUTH_CLIENT_SECRET=[Production client secret]

# Subscription Services
STRIPE_SECRET_KEY=[Production Stripe key]
REVENUECAT_API_KEY=[Production RevenueCat key]

# Push Notifications
FIREBASE_SERVICE_ACCOUNT_KEY=[Production Firebase key]

# App Configuration
APP_URL=https://mybranches.app
```

### Development vs Production Settings

#### Capacitor Server Configuration
```typescript
server: {
  androidScheme: 'https',
  // Only use dev server in development
  url: process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : undefined,
  cleartext: process.env.NODE_ENV === 'development',
  allowNavigation: process.env.NODE_ENV === 'development' ? [
    '*.replit.dev',
    'http://localhost:*',
  ] : []
}
```

## 7. Build Scripts and Commands

### iOS Production Build
```bash
# 1. Build web assets
npm run build

# 2. Sync with Capacitor
npx cap sync ios

# 3. Open in Xcode for archive
npx cap open ios

# 4. In Xcode: Product > Archive > Distribute App
```

### Android Production Build
```bash
# 1. Build web assets
npm run build

# 2. Sync with Capacitor
npx cap sync android

# 3. Build release APK/AAB
cd android
./gradlew assembleRelease
# or for App Bundle:
./gradlew bundleRelease
```

## 8. App Store Compliance Features

### Privacy-First Design ✅
- Family-only networks (no public posting)
- COPPA-compliant for children
- Transparent data practices
- Secure authentication via Replit Auth

### Subscription Compliance ✅
- Clear pricing display ($5.99/month or $60/year)
- Household-level subscription sharing
- Easy cancellation process
- Platform-appropriate billing (Stripe web, RevenueCat mobile)

### Content Guidelines Compliance ✅
- Family-friendly content only
- No user-generated public content
- Private family group communication
- Appropriate for all ages (4+ rating)

## 9. Pre-Submission Checklist

### Technical Requirements
- [ ] App builds successfully for both iOS and Android
- [ ] All features work in production build
- [ ] Deep linking works correctly
- [ ] Push notifications function properly
- [ ] Subscription system works end-to-end
- [ ] Database connections are production-ready

### Content Requirements
- [ ] App store descriptions are compelling and accurate
- [ ] Screenshots showcase key features
- [ ] Privacy Policy is accessible via URL
- [ ] Terms of Service is accessible via URL
- [ ] Support contact information is available

### Legal Requirements
- [ ] Privacy Policy covers all data collection
- [ ] Terms of Service includes subscription terms
- [ ] COPPA compliance for family app
- [ ] Appropriate content rating assigned

## 10. Post-Launch Monitoring

### Key Metrics to Track
- **App Store Performance**: Downloads, ratings, reviews
- **User Engagement**: Daily/monthly active families
- **Subscription Conversion**: Free to premium upgrade rate
- **Technical Health**: Crash rates, performance metrics
- **User Feedback**: Reviews and support requests

### Update Cadence
- **Bug Fixes**: As needed (hot fixes for critical issues)
- **Feature Updates**: Monthly or bi-monthly
- **Major Releases**: Quarterly with significant new features

---

**This configuration ensures My Branches is ready for professional app store submission while maintaining the family-focused, privacy-first approach that makes it unique in the market.**