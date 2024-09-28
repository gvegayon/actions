# Post artifact as a comment

## Example: Post artifact as a comment

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

      # Post the artifact with id `readme` as a comment.
      # The msg will refer to the arfitact as 'README file'.
      - name: Post the artifact
        uses: gvegayon/actions/post-artifact
        with:
          artifact-id: readme
          artifact-name: 'README file'
```

For a live example, see [../.github/workflows/test-post-artifact.yml](../.github/workflows/test-post-artifact.yml).

