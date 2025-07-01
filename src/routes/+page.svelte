<script>
    import MRPartCard from "../components/MRPartCard.svelte";
    import mridata from "$lib/mridata.json";
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

</style>

<div class="maincontent">
    <div class="header">
        <div class="header-text">
            MR Protokoll [Work in Progress]
        </div>
        <div class="header-subtext">
            Här finner du alla MR protokoll som används på buk och kärl sektionen.
        </div>
    </div>
    <div class="cards">
        {#each mridata as indata} 
          <MRPartCard part_name={indata.partname}
                      input_data={indata.data}
                      --card-color={indata.color} />
        {/each}
    </div>
</div>