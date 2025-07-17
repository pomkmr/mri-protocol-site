<script>
    let {input_data} = $props();
    import test_html from '$lib/clean_test.html?raw'

</script>

<style>
    .maincontent {
        width: 100%;
        height: 200px;
    }

    .maintable {
        margin-top: 40px;
    }

    .text-div {
        margin: 10px 0;
        font-weight: bold;
    }

    table {
        table-layout: fixed;
        border-collapse: collapse;
        border: 1px solid black;
    }

    th,
    td {
        padding: 10px;
        background-color: inherit;
        color: inherit;
    }

    th {
        text-align: left;
    }

    tbody tr:nth-child(odd) {
        background-color: gainsboro;
    }

</style>

<div class="maincontent">
    <div class="mainheader">
        <div class="text-div">
            <span class="text-label">Indikationer</span>:
        </div>
        <div class="text-div">
            <span class="text-label">Förberedelser</span>: 
        </div>
        <div class="text-div">
            <span class="text-label">System</span>: 
        </div>
        <div class="text-div">
            <span class="text-label">Spole</span>: 
        </div>
        <div class="text-div">
            <span class="text-label">Kontrast</span>: 
        </div>
        <div class="text-div">
            <span class="text-label">Undersökningskod</span>: 
        </div>
        <div class="text-div">
            <span class="text-label">Undersökningstid</span>: 
        </div>
    </div>
    <div class="maintable">
        <table>
            <thead>
                <tr>
                    <th scope="col">Skevens</th>
                    <th scope="col">Snittplan</th>
                    <th scope="col">Snitttjockleck</th>
                    <th scope="col">Täckningsområde, vinkling mm</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Survey</td>
                    <td>3 plan</td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </div>
    {@html test_html}
</div>