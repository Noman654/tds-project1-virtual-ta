#!/usr/bin/env python3
"""
API Key Validation Script
This script helps validate your aipipe API token configuration.
"""

import os
import sys
from dotenv import load_dotenv

def validate_api_key():
    """Validate the API key configuration"""
    print("🔍 Checking aipipe API token configuration...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ No .env file found")
        print("   Please create a .env file based on .env.example")
        return False
    
    # Check if AIPIPE_TOKEN is set (for backward compatibility, also check API_KEY)
    aipipe_token = os.getenv("AIPIPE_TOKEN") or os.getenv("API_KEY")
    if not aipipe_token:
        print("❌ AIPIPE_TOKEN not found in environment variables")
        print("   Please add your aipipe token to the .env file:")
        print("   AIPIPE_TOKEN=eyJhbGciOiJIUzI1NiJ9.your_token_here")
        return False
    
    # Validate aipipe token format (JWT tokens typically have 3 parts separated by dots)
    if not (aipipe_token.count('.') == 2 and aipipe_token.startswith("eyJ")):
        print("❌ Aipipe token format appears incorrect")
        print(f"   Your token starts with: {aipipe_token[:10]}...")
        print("   Aipipe tokens should be JWT format (eyJ...)")
        return False
    
    # Check token length (basic validation)
    if len(aipipe_token) < 100:
        print("❌ Aipipe token appears too short")
        print("   JWT tokens are typically much longer")
        return False
    
    print("✅ Aipipe token configuration looks good!")
    print(f"   Token starts with: {aipipe_token[:20]}...")
    print(f"   Token length: {len(aipipe_token)} characters")
    
    return True

def test_api_connection():
    """Test basic connection to aipipe API"""
    try:
        import aiohttp
        import asyncio
        import json
        
        async def test_connection():
            aipipe_token = os.getenv("AIPIPE_TOKEN") or os.getenv("API_KEY")
            
            # Test the models endpoint as shown in the curl example
            url = "https://aipipe.org/openai/v1/models"
            headers = {
                "Authorization": aipipe_token  # aipipe uses direct token, not Bearer
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        print("✅ Aipipe API connection successful!")
                        data = await response.json()
                        if 'data' in data and len(data['data']) > 0:
                            print(f"   Available models: {len(data['data'])} models found")
                            # Show first few models
                            for i, model in enumerate(data['data'][:3]):
                                print(f"   - {model.get('id', 'Unknown')}")
                        return True
                    elif response.status == 401:
                        print("❌ Authentication failed")
                        error_text = await response.text()
                        print(f"   Error: {error_text}")
                        return False
                    else:
                        print(f"❌ API request failed with status {response.status}")
                        error_text = await response.text()
                        print(f"   Error: {error_text}")
                        return False
        
        print("\n🔗 Testing aipipe API connection...")
        return asyncio.run(test_connection())
        
    except ImportError:
        print("⚠️  Cannot test API connection (missing dependencies)")
        print("   Run: pip install aiohttp")
        return None
    except Exception as e:
        print(f"❌ Error testing API connection: {e}")
        return False

def main():
    """Main validation function"""
    print("Aipipe API Token Validator")
    print("=" * 30)
    
    # Validate API key configuration
    if not validate_api_key():
        print("\n❌ Please fix the aipipe token configuration and try again.")
        sys.exit(1)
    
    # Test API connection
    connection_result = test_api_connection()
    
    if connection_result is True:
        print("\n🎉 Everything looks good! You can now run the preprocessing script.")
    elif connection_result is False:
        print("\n❌ Aipipe API connection failed. Please check your token and try again.")
        sys.exit(1)
    else:
        print("\n⚠️  Aipipe token format is correct, but couldn't test connection.")
        print("   You can try running the preprocessing script.")

if __name__ == "__main__":
    main()
