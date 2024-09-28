# Post artifact as a comment

## Example: Post artifact created within a job

Here are the contents of a job that (i) uploads an artifact using `actions/upload-artifact` and (ii)
posts the artifact as a comment using this action.


```yaml
    # Required permissions
    permissions:
      contents: read
      pull-requests: write
    env:
      GH_TOKEN: ${{ github.token }}

    steps:
      - uses: actions/checkout@v4
        name: Checkout code

      # Uploading an artifact with id 'readme'
      - uses: actions/upload-artifact@v4
        name: Upload artifact
        id: readme
        with:
          path: './README.md'

      # Post the artifact pulling the id from the `readme` step.
      # The msg will refer to the arfitact as 'README file'.
      - name: Post the artifact
        uses: gvegayon/actions/post-artifact
        with:
          artifact-id: ${{ steps.readme.outputs.artifact-id }}
          artifact-name: 'README file'
```

For a live example, see [../.github/workflows/test-post-artifact.yml](../.github/workflows/test-post-artifact.yml).

## Example: Post an artifact created in a previous job

When passing between jobs, the artifact id can be passed as an output. Here is an example of how to do it:

```yaml
jobs:

  build:

    runs-on: ubuntu-latest

    # Expose the artifact id as an output
    outputs:
      artifact-id: ${{ steps.upload.outputs.artifact-id }}

    steps:
      - uses: actions/checkout@v4
        name: Checkout code

      # Uploading an artifact with id 'readme'
      - uses: actions/upload-artifact@v4
        name: Upload artifact
        id: upload
        with:
          path: './README.md'

  post:
    runs-on: ubuntu-latest
    
    # This job depends on the `build` job
    needs: build

    # Required permissions
    permissions:
      contents: read
      pull-requests: write
    env:
      GH_TOKEN: ${{ github.token }}

    steps:
      # Post the artifact pulling the id from the `readme` step.
      # The msg will refer to the arfitact as 'README file'.
      - name: Post the artifact
        uses: gvegayon/actions/post-artifact
        with:
          artifact-id: ${{ needs.build.outputs.artifact-id }}
          artifact-name: 'README file'

```