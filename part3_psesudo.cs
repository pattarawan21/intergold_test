

public DataTable GetCustomerInfo(string id, DateTime? startDate = null, DateTime? endDate = null)
{
    var dt = new DataTable();
    using (var conn = new SqlConnection("...")) // Connection string is hardcoded
    {
        conn.Open();
        var sql = "SELECT * FROM Customer WHERE id = '" + id + "'";

        if (startDate.HasValue)
        {
            sql += " AND created_at >= '" + startDate.Value.ToString("yyyy-MM-dd HH:mm:ss") + "'";
        }
        if (endDate.HasValue)
        {
            sql += " AND created_at <= '" + endDate.Value.ToString("yyyy-MM-dd HH:mm:ss") + "'";
        }

        using (var da = new SqlDataAdapter(sql, conn))
        {
            da.Fill(dt);
        }
    }
    return dt;
}