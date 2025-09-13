# 🔐 SECURE ANDROID SIGNING INSTRUCTIONS

## 🚨 CRITICAL SECURITY ISSUE RESOLVED

The previous Android keystore was **compromised** (stored in repository with hardcoded passwords). This has been fixed:

✅ **Removed** compromised keystore from repository  
✅ **Updated** .gitignore to exclude all keystores  
✅ **Secured** build.gradle to use environment variables  

## 📱 GENERATING YOUR SECURE UPLOAD KEYSTORE

**You MUST generate a new keystore manually for security:**

```bash
# Generate your secure upload keystore
keytool -genkey -v -keystore upload-keystore.jks \
    -alias upload -keyalg RSA -keysize 2048 -validity 10000 \
    -dname "CN=MyBranches,OU=Development,O=MyBranches,L=San Francisco,ST=CA,C=US"

# When prompted, enter:
# - Keystore password: [Generate a strong password - save it securely]
# - Key password: [Same or different strong password - save it securely]
```

## 🔑 SECURE SIGNING CONFIGURATION

**Create `android/gradle.properties` file:**

```properties
# Android Signing (NEVER commit these values)
ANDROID_STORE_FILE=upload-keystore.jks
ANDROID_STORE_PASSWORD=your_secure_store_password
ANDROID_KEY_ALIAS=upload
ANDROID_KEY_PASSWORD=your_secure_key_password
```

## 🏗️ BUILD SIGNED ANDROID APP BUNDLE

```bash
# Navigate to android directory
cd android

# Build signed AAB
./gradlew bundleRelease
```

**✅ Output:** `android/app/build/outputs/bundle/release/app-release.aab`

## 📦 GOOGLE PLAY STORE SUBMISSION

1. **Upload to Google Play Console**
   - Go to Google Play Console → App releases → Production
   - Upload `app-release.aab`
   - Package name: `com.mybranches.app`
   - Version: 1.0 (code: 1)

2. **Enable Google Play App Signing** (Recommended)
   - Let Google manage your app signing key
   - Your upload key remains private
   - Better security and key management

3. **Update SHA256 Fingerprint**
   - After upload, get SHA256 from Play Console → App integrity
   - Replace `PLACEHOLDER_UPDATE_AFTER_PLAY_STORE_UPLOAD` in your code
   - Redeploy backend for Universal Links to work

## 🔒 SECURITY BEST PRACTICES

- **NEVER** commit keystores to repositories
- **NEVER** hardcode passwords in build files  
- **BACKUP** your upload keystore securely (losing it means you can't update your app)
- **USE** strong, unique passwords for keystore and keys
- **STORE** passwords in secure password manager

## ⚠️ IMPORTANT NOTES

- The old compromised keystore has been removed and secured
- You must generate a NEW keystore before submission
- Google Play Store will reject unsigned or improperly signed AABs
- Keep your upload keystore PRIVATE and SECURE

---

**Status: Ready for secure signing and Google Play Store submission** 🚀