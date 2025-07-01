<script>
    import '../main.css';
    export const prerender = true;
    let {children} = $props();
</script>

{@render children()}