# Firebase Setup Instructions for My Branches

## Android App Firebase Configuration

To enable push notifications and proper Firebase integration for your Android app, you need to create a Firebase project and download the configuration file.

### Steps:

1. **Create Firebase Project**
   - Go to https://console.firebase.google.com
   - Click "Create a project"
   - Project name: "My Branches"
   - Enable Google Analytics (recommended)

2. **Add Android App**
   - Click "Add app" → "Android"
   - Package name: `com.mybranches.app`
   - App nickname: "My Branches Android"
   - SHA-1 certificate fingerprint: (optional for development)

3. **Download Configuration**
   - Download `google-services.json`
   - Place it in: `android/app/google-services.json`

4. **Enable Cloud Messaging**
   - In Firebase Console → Project Settings → Cloud Messaging
   - Note the Server Key for backend integration

5. **Test Integration**
   - Rebuild Android app: `cd android && ./gradlew bundleRelease`
   - Verify push notifications work

### Environment Variables Needed:
```bash
# Frontend (add to .env)
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=mybranches.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=mybranches
VITE_FIREBASE_STORAGE_BUCKET=mybranches.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id

# Backend (add to secrets)
FIREBASE_SERVICE_ACCOUNT_KEY=your_service_account_json
```

This will resolve the FCM integration issues and enable full push notification functionality.