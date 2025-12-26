# GitHub Actions Setup for Private Submodule

## Current Issue

GitHub Actions cannot access the private `openterface-cms` submodule. This is a common issue with private submodules.

## Solutions

### Solution 1: Organization Settings (Recommended)

If both repos are in the same organization (`TechxArtisanStudio`):

1. Go to organization settings: https://github.com/organizations/TechxArtisanStudio/settings/actions
2. Under "Workflow permissions", ensure:
   - ✅ "Read and write permissions" is selected
   - ✅ "Allow GitHub Actions to create and approve pull requests" is enabled
3. Under "Actions secrets and variables", verify access settings

**Note**: `GITHUB_TOKEN` should automatically have access to private repos in the same org, but org settings might restrict this.

### Solution 2: Use Personal Access Token (PAT)

If `GITHUB_TOKEN` doesn't work, create a PAT:

1. **Create PAT**:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Name: `openterface-cms-access`
   - Scopes: Select `repo` (full control of private repositories)
   - Generate and copy the token

2. **Add as Secret**:
   - Go to main repo: https://github.com/TechxArtisanStudio/Openterface/settings/secrets/actions
   - Click "New repository secret"
   - Name: `CMS_ACCESS_TOKEN`
   - Value: Paste the PAT
   - Add secret

3. **Update Workflow**:
   ```yaml
   - uses: actions/checkout@v4
     with:
       fetch-depth: 0
       submodules: recursive
       token: ${{ secrets.CMS_ACCESS_TOKEN }}  # Use PAT instead
   ```

### Solution 3: Verify Repository Exists

1. Check repository exists: https://github.com/TechxArtisanStudio/openterface-cms
2. Verify it's set to **Private**
3. Ensure you have access to it

### Solution 4: Check .gitmodules

Ensure `.gitmodules` uses HTTPS:
```ini
[submodule "openterface-cms"]
    path = openterface-cms
    url = https://github.com/TechxArtisanStudio/openterface-cms.git
```

## Current Configuration

- ✅ `.gitmodules` uses HTTPS URL
- ✅ Workflow uses `GITHUB_TOKEN`
- ✅ `submodules: recursive` enabled
- ⚠️ May need PAT if GITHUB_TOKEN doesn't have access

## Testing

After applying a solution, trigger the workflow:
1. Make a small change and push, OR
2. Go to Actions tab → "Run workflow" → Select branch → Run

## Quick Fix: Use PAT

If you want to quickly fix this, create a PAT and update the workflow:

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
    submodules: recursive
    token: ${{ secrets.CMS_ACCESS_TOKEN }}  # Change this line
```

Then add `CMS_ACCESS_TOKEN` secret with your PAT value.

