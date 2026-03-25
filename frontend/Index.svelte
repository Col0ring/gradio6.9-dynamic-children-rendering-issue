<script lang="ts">
  import { Gradio } from '@gradio/utils'

  const props = $props()
  // Read props to clean up the loading effect
  new Gradio(props)

  const promise = new Promise<string>((resolve) => {
    setTimeout(() => {
      resolve('hello')
    }, 500)
  })
</script>

{#await promise then value}
  <div>
    {value}
    <!-- not working -->
    {@render props.children?.()}
  </div>
{/await}

<!-- worked -->
<!-- {@render props.children?.()} -->
