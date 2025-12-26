# Setup Personal Access Token for Private Submodule

## Why PAT is Needed

Even though both repositories are in the same organization (`TechxArtisanStudio`), `GITHUB_TOKEN` **does not automatically have access** to private repositories. This is a known GitHub limitation - `GITHUB_TOKEN` is scoped only to the repository that triggers the workflow.

## Solution: Create and Use Personal Access Token

### Step 1: Create Personal Access Token (PAT)

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Configure the token:
   - **Note**: `openterface-cms-github-actions`
   - **Expiration**: Choose appropriate expiration (e.g., 1 year, or no expiration)
   - **Scopes**: Check **`repo`** (Full control of private repositories)
     - This includes all sub-scopes: `repo:status`, `repo_deployment`, `public_repo`, `repo:invite`, `security_events`
4. Click **"Generate token"**
5. **IMPORTANT**: Copy the token immediately - you won't be able to see it again!

### Step 2: Add PAT as Repository Secret

1. Go to your main repository: https://github.com/TechxArtisanStudio/Openterface/settings/secrets/actions
2. Click **"New repository secret"**
3. Configure the secret:
   - **Name**: `CMS_ACCESS_TOKEN`
   - **Secret**: Paste the PAT token you copied
4. Click **"Add secret"**

### Step 3: Verify Workflow Configuration

The workflow is already configured to use the PAT:
```yaml
token: ${{ secrets.CMS_ACCESS_TOKEN || secrets.GITHUB_TOKEN }}
```

This will:
- Try `CMS_ACCESS_TOKEN` first (your PAT)
- Fall back to `GITHUB_TOKEN` if PAT is not set

### Step 4: Test

1. Make a small change and push to trigger the workflow, OR
2. Go to Actions tab → "Run workflow" → Select branch → Run

The workflow should now successfully checkout the private `openterface-cms` submodule.

## Alternative: Organization-Level Secret

If you want to use this PAT across multiple repositories in your organization:

1. Go to: https://github.com/organizations/TechxArtisanStudio/settings/secrets/actions
2. Click **"New organization secret"**
3. Configure:
   - **Name**: `CMS_ACCESS_TOKEN`
   - **Secret**: Paste the PAT
   - **Repository access**: Select "Selected repositories" and choose `Openterface`
4. Click **"Add secret"**

Then update the workflow to reference the org secret:
```yaml
token: ${{ secrets.CMS_ACCESS_TOKEN || secrets.GITHUB_TOKEN }}
```

## Security Notes

- **Never commit the PAT to the repository**
- **Use repository secrets** (not environment variables) for PATs
- **Rotate the PAT periodically** for security
- **Use minimal scopes** - only `repo` scope is needed
- **Consider expiration dates** for better security

## Troubleshooting

If it still doesn't work:
1. Verify the PAT has `repo` scope
2. Verify the secret name is exactly `CMS_ACCESS_TOKEN`
3. Check the workflow logs for detailed error messages
4. Verify the `openterface-cms` repository exists and is private

