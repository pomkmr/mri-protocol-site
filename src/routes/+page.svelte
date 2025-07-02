<script>
    import MRPartCard from "../components/MRPartCard.svelte";
    import mridata from "$lib/mridata.json";

    let searchterm = $state('');
</script>

<style>
    .maincontent {
        margin: 0 auto;
    }

    .header {
        margin: 10px;
    }

    .header-text {
        font-size: 2rem;
        font-weight: bold;
        color: var(--main-text-color);
    }

    .header-subtext{
        font-size: 1.5rem;
        font-weight: 500;
        line-height: 1.5;   
    }

    .search-div {
        margin: 20px auto;
        width: 200px;
    }

    .search-div input {
        height: 40px;
        vertical-align: bottom;
        font-size: 1.1rem;
    }

</style>

<div class="maincontent">
    <div class="header">
        <div class="header-text">
            MR Protokoll [Work in Progress]
        </div>
        <div class="header-subtext">
            Här finner du MR protokoll som används på buk och kärl sektionen. Filtrera efter indikation med hjälp av sökrutan.
        </div>
        <div class="search-div">
            <input type="text" bind:value={searchterm} placeholder="indikation">
        </div>
    </div>
    <div class="cards">
        {#each mridata as indata} 
          <MRPartCard part_name={indata.partname}
                      input_data={indata.data}
                      search_term={searchterm}
                      --card-color={indata.color} />
        {/each}
    </div>
</div>