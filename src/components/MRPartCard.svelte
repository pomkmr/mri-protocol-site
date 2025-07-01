<script>
    let {part_name, input_data} = $props();


    let show_info = $state(false);
    import sample_img from "$lib/images/sample_mri.jpg";
    
    import Modal from "./Modal.svelte";
    let showModal = $state(false);
    let show_table = $state(false);

    import ProtoInfo from "./ProtoInfo.svelte";

    let abv_number = $state('');
    let name = $state('');

    function get_extra_info(info) {
        abv_number = info.abv;
        name = info.name;
        showModal = true;
    }
</script>

<style>
    .card-container {
        border: 2px solid gray;
        margin: 20px;
        overflow: hidden;

        box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
        transition: box-shadow 0.3s ease;
    }

    .card-container:hover {
        box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
    }

    table {
        table-layout: fixed;
        border-collapse: collapse;
    }

    caption {
        padding: 1.2rem;
        background-color: var(--card-color);
        text-align: left;
        width: 100%;
        font-weight: bold;
        font-size: 1.5rem;
        caption-side: top;
        letter-spacing: 1px;
        color: white;   
    }

    th,
    td {
        padding: 10px 20px;
        background-color: inherit;
        color: inherit;
    }

    th {
        text-align: left;
    }

    tbody tr:nth-child(odd) {
        background-color: gainsboro;
    }

    tbody tr:hover {
        cursor: pointer;
        color: white;
        background-color: var(--card-color);
    }


    .image-container {
        border: 2px solid gray;
        background-color: gainsboro;
        padding: 20px;
    }

     .image {
        border: 2px solid gray;
        border-radius: 10px;
        overflow: hidden;
    }

    .image img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    caption:hover {
        background-color: green;
        cursor: pointer;
    }

</style>


<Modal bind:showModal>
	{#snippet header()}
		<h2>
			{abv_number} {name}
		</h2>
	{/snippet}
    {#snippet children()}
        <ProtoInfo input_data={name}/>
    {/snippet}
</Modal>

<div class="card-container">
    <table>
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
        <caption onclick={() => show_table = !show_table}>
            {part_name}
        </caption>

        {#if show_table}

        <thead>
            <tr>
                <th scope="col">Kod</th>
                <th scope="col">Namn</th>
                <th scope="col">Protokoll</th>
                <th scope="col">Tid</th>
                <th scope="col">Indikationer</th>
            </tr>
        </thead>
        <tbody>
            {#each input_data as rowdata}
            <tr onclick={() => get_extra_info(rowdata)}>
                <td>{rowdata.abv}</td>
                <td>{rowdata.name}</td>
                <td>{rowdata.code}</td>
                <td>{rowdata.time}</td>
                <td>{rowdata.desc}</td>
            </tr>
            
            <!-- {#if show_info}
                <tr >
                    <td colspan="5" class="image-container">
                        <div class="images-div">
                            <img src={sample_img} alt="test">
                        </div>
                    </td>
                </tr>
            {/if} -->

            {/each}
        </tbody>
        {/if}
    </table>
</div>