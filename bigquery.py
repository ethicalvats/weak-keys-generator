from google.cloud import bigquery
client = bigquery.Client()


def make(address):
    query = (
        f"""
            with double_entry_book as (
                -- debits
                select to_address as address, value as value
                from `bigquery-public-data.ethereum_blockchain.traces`
                where to_address is not null
                and status = 1
                and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
                union all
                -- credits
                select from_address as address, -value as value
                from `bigquery-public-data.ethereum_blockchain.traces`
                where from_address is not null
                and status = 1
                and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
                union all
                -- transaction fees debits
                select miner as address, sum(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value
                from `bigquery-public-data.ethereum_blockchain.transactions` as transactions
                join `bigquery-public-data.ethereum_blockchain.blocks` as blocks on blocks.number = transactions.block_number
                group by blocks.miner
                union all
                -- transaction fees credits
                select from_address as address, -(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value
                from `bigquery-public-data.ethereum_blockchain.transactions`
            )
            select address, sum(value) as balance
            from double_entry_book
            where address = '{address}'
            group by address
            order by balance desc
            limit 10
        """
    )
    # print(query)
    query_job = client.query(query)
    return query_job
